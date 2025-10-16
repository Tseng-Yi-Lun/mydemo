from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 假資料庫：文章列表 (你可以用 SQLite 取代這個列表)
posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        posts.append({
            'title': title,
            'author': author,
            'content': content
        })

        return redirect(url_for('index'))
    
    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
