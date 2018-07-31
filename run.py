import os

from application import create_app

if __name__ == '__main__':
    app = create_app('development')
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)

    #checkout flask run method
    #proper use of exceptions
    # remove unused dependencies
    #remove unnecessary files from nosetests with coverage