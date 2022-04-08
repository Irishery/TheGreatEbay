from flask import Blueprint, render_template

main_route = Blueprint("main_route", __name__)

@main_route.route("/")
@main_route.route('/main')
def index():
    puctures = {
                "contents": [
                    {
                        "title": "https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-13.jpg",
                        "content": "$5"
                    },
                    {
                        "title": "https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-13.jpg",
                        "content": "$6"
                    },
                    {
                        "title": "https://proprikol.ru/wp-content/uploads/2021/01/sobachki-krasivye-kartinki-13.jpg",
                        "content": "$4"
                    },
                    {
                        "title": "https://kartinkin.net/uploads/posts/2021-07/thumbs/1625296547_11-kartinkin-com-p-french-dog-yeda-krasivo-foto-57.jpg",
                        "content": "$5"
                    },
                    {
                        "title": "https://kartinkin.net/uploads/posts/2021-07/thumbs/1625296547_11-kartinkin-com-p-french-dog-yeda-krasivo-foto-57.jpg",
                        "content": "$6"
                    },
                    {
                        "title": "https://kartinkin.net/uploads/posts/2021-07/thumbs/1625296547_11-kartinkin-com-p-french-dog-yeda-krasivo-foto-57.jpg",
                        "content": "$4"
                    }

                        ]
                }
    return render_template('index.html', pics=puctures)
