from app import create_app

def run_app():
    """Run the development server"""
    environment_config = 'dev_config'
    app_instance = create_app(environment_config)
    app_instance.run()

if __name__ == '__main__':
    run_app()

