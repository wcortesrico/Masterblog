from flask import Flask, render_template, request, redirect, url_for
import json

app = Flask(__name__)

@app.route("/")
def index():
    with open("blog_post.json", "r") as data_file:
        blog_posts = json.loads(data_file.read())

    return render_template('index.html', posts=blog_posts)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        with open("blog_post.json", "r") as data_file:
            blog_posts = json.loads(data_file.read())
        max_id = 0
        for post in blog_posts:
            if post["id"] > max_id:
                max_id = post["id"]
        new_id = max_id + 1
        title_from_form = request.form.get("title")
        author_from_form = request.form.get("author")
        content_from_form = request.form.get("content")
        new_post_dict = {"id": new_id, "author": author_from_form, "title": title_from_form, "content": content_from_form}
        blog_posts.append(new_post_dict)
        blog_posts_json = json.dumps(blog_posts)
        with open("blog_post.json", "w") as new_file:
            new_file.write(blog_posts_json)

        return redirect(url_for('index'))
    return render_template("add.html")

@app.route("/delete/int:<post_id>")
def delete(post_id):
    with open("blog_post.json", "r") as data_file:
        blog_posts = json.loads(data_file.read())
    for blog in blog_posts:
        if int(post_id) == int(blog['id']):
            blog_posts.remove(blog)

    blog_posts_json = json.dumps(blog_posts)
    with open("blog_post.json", "w") as new_file:
        new_file.write(blog_posts_json)

    return redirect(url_for('index'))



if __name__ == "__main__":
    app.run()