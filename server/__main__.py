from server import init_api
from server.configuration import environment


def main():  # pragma: no cover
    """
    Main function for fileuploader server
    """
    app = init_api()
    app.run(host=environment.HOST, port=environment.PORT, debug=False)


if __name__ == "__main__":  # pragma: no cover
    main()
