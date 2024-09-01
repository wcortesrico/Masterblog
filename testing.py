if request.method == "POST":
    # Update the post in the JSON file
    # Redirect back to index
    title_from_form = request.form.get("title")
    author_from_form = request.form.get("author")
    content_from_form = request.form.get("content")
    with open("blog_post.json", "r") as data_file:
        blog_posts = json.loads(data_file.read())
    for post in blog_posts:
        if int(post["id"]) == int(post_id):
            post["title"] = title_from_form
            post["author"] = author_from_form
            post["content"] = content_from_form

    blog_posts_json = json.dumps(blog_posts)
    with open("blog_post.json", "w") as new_file:
        new_file.write(blog_posts_json)

    return redirect(url_for("index"))

elif request.method == "GET":