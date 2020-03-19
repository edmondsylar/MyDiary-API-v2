from application import create_app

app = create_app('production')

if __name__ == '__main__':
    #app = create_app('development')
    app.run()
