
# secrets.py

# Import the configparser library
import configparser

# Create a new ConfigParser object
config = configparser.ConfigParser()

# Read the secrets.ini file
config.read('secrets.ini')

# Create a dictionary called 'secrets'
secrets = config['apikey']

# Retrieve the API key
api_key = secrets['api_key']

#  4. Import the secrets.py file into your main.py file.
#  5. Use the api_key variable to access your API key.
#  6. Add the secrets.ini and secrets.py files to your .gitignore file.
#  7. Push your code to GitHub.
#  8. Create a new repository on GitHub called weather-app.
#  9. Push your code to the new repository.
# 10. Create a new branch called secrets.
# 11. Push your code to the secrets branch.
# 12. Create a pull request to merge the secrets branch into the master branch.
# 13. Merge the pull request.
# 14. Delete the secrets branch.
