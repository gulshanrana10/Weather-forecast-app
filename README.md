<h3>Purvanuman              <a href="https://drive.google.com/file/d/1cy-6oM2mn3tFoEJxiZ75KFYz4boJ4XLp/view?usp=sharing">(Video link)</a>     </h3>  

Purvanuman powered by Github Copilot – a Python command line tool for displaying weather forecasts.  It utilizes Open Weather Map to fetch data using a API call and requests the data using Python’s request Memory by leveraging APIs and the user's input, the tool fetches the current weather data and displays it in a user-friendly format. It requests data by making an API call to the Open Weather Map service provider using Python's requests library. The tool is very simple. The user is navigated by specific and simple instructions. Weather forecasts are also displayed in a table using Python's PrettyTable library.

Upon running the program, the user is prompted to enter the name of the city for which they desire the weather forecast. Once the city name is entered, the tool initiates a request to a weather API (such as OpenWeatherMap) to retrieve the relevant weather data.
To enhance the user experience, the program uses various fonts to stylize the output. The weather information is presented in a visually appealing format, making it easy for users to read and understand.
The weather forecast tool provides essential weather details such as temperature, humidity, pressure, and an overall description of the weather condition (e.g., sunny, cloudy, rainy) for the specified city. This enables users to stay informed about the current weather conditions in any location of their interest.
Overall, this Python project combines functionality, aesthetics, and user experience enhancements to create a user-friendly weather forecast tool in the command line.
<br/><br/>
<b>Table of Contents</b>
<li>Objective</li>
<li>Motivation</li>
<li>Functional Requirements</li>
<li>Architectural Diagram</li>
<li>Existing Features</li>
<li>Future Scope</li>
<li>Technologies Used</li>
<li>Python Libraries</li>
<li>Installation</li>
<li>Github Copilot Assistance</li>
<li>Usage</li>
<li>Error Handling</li>
<li>Conclusion</li>
<br/>
<b>Objective</b><br/>
The primary goal of the project is to develop a simple command line tool using the Python programming language. In addition, one of the most important purposes of the application is to request data from service providers using API and to display this data on the screen in a format that the user can read.
The objectives of the Purvanuman project, a Python command line tool for displaying weather forecasts, powered by Github Copilot and utilizing Open Weather Map API, can include the following:<br/>
<ol>
<li>Fetching Weather Data: The primary objective is to retrieve weather data from the Open Weather Map API by making API calls using Python's requests library. The tool should be able to gather the necessary information, such as temperature, humidity, wind speed, and other relevant data.</li>

<li>User-Friendly Interface: The tool should provide a straightforward and easy-to-use interface, guiding the user through specific and simple instructions. It should allow users to input their desired location or query to retrieve weather forecasts accurately.</li>

<li>Displaying Current Weather: Once the weather data is fetched, the tool should present the current weather information in a user-friendly format. This could include displaying the temperature, weather condition, humidity, wind speed, and any other relevant details that provide a comprehensive overview of the current weather.</li>

<li>Forecast Display: In addition to the current weather, the tool should also be capable of displaying weather forecasts for upcoming days. It should leverage Python's PrettyTable library to present the forecast data in a well-formatted and easily understandable tabular or graphical format.</li>

<li>Error Handling: The tool should incorporate robust error handling mechanisms to handle scenarios where API calls fail or incorrect user inputs are provided. It should provide appropriate error messages or instructions to guide the user in resolving any issues encountered during the weather data retrieval process.</li>

<li>Code Efficiency and Best Practices: The project should adhere to good coding practices, such as modularization, code reusability, and efficient resource utilization. It should follow Python coding conventions, making the code readable, maintainable, and scalable.</li>

<li>Documentation and Readme: The project should include comprehensive documentation and a README file that provides clear instructions on how to set up, install dependencies, and use the tool effectively. It should also provide examples and sample outputs to help users understand the capabilities and usage of the tool.</li>

<li>Testing and Validation: It is essential to conduct thorough testing to ensure the tool functions correctly and provides accurate weather information. Test cases should cover different scenarios and edge cases, including handling various input types and error conditions.</li>
</ol>

<b>Motivation</b><br/>
The motivation behind the Purvanuman project, a Python command line tool for displaying weather forecasts, can stem from several factors:
<ol>
<li>Weather Information Accessibility: Weather forecasts play a crucial role in various aspects of daily life, including planning outdoor activities, travel arrangements, and decision-making related to clothing or equipment. The project aims to provide a convenient and accessible way for users to retrieve weather information directly from the command line, eliminating the need for manual browsing or relying on external weather apps or websites.</li>

<li>Developer Learning and Skill Enhancement: The project allows developers to practice and enhance their Python programming skills by implementing functionalities like API integration, data retrieval, error handling, and user interface design. It serves as a practical learning opportunity for leveraging third-party APIs, handling data, and creating command line tools.</li>

<li>Open Weather Map API Integration: By utilizing the Open Weather Map API, the project showcases the integration of external services and APIs into Python applications. It demonstrates how to make API calls, handle responses, and extract relevant weather data for further processing and display.</li>

<li>Personalized Weather Experience: The project provides an opportunity for users to retrieve weather information tailored to their specific location or query. It enables users to quickly access accurate and up-to-date weather data without having to navigate through complex interfaces or advertisements commonly found in weather websites or apps.</li>

<li>Code Assistance with GitHub Copilot: The project's integration with GitHub Copilot, a code generation AI tool, can assist developers in generating code snippets and providing suggestions during the development process. This collaboration between human developers and AI tools aims to enhance productivity and code quality.</li>

<li>Exploration of Python Libraries: The project incorporates Python libraries such as requests and PrettyTable to facilitate API communication and enhance the presentation of weather data. By utilizing these libraries, developers can explore their features, understand their usage, and leverage them for future projects.</li></ol>

Overall, the motivation behind the Purvanuman project lies in creating a convenient and customizable weather forecast tool, fostering developer learning and skill enhancement, integrating external APIs, and leveraging AI-powered code assistance to streamline the development process.

<b>Functional Requirements</b>
Here are some user experience criteria that were considered while developing the application:
<ul>
<li>As a user, I would like to see a simple interface.</li>
<li>As a user, I don't want to read too much content.</li>
<li>As a user, I would like to see the weather forecast of the city I am looking for in a proper format.</li>
<li>As a user, I would like to see clear navigation.</li>
<li>As a user, I don't want to enter too many inputs to use the app.</li></ul>  
The application has been developed considering the above criteria.
<br/>
<br/>
<b>Architectural Diagram</b><br/>
<img src="https://github.com/Fastest-Coder-First/Bsquare/blob/main/weather-app/architectural_flow.jpeg" alt="architectural diagram no-preview">

<ol>
 <li>User Input:
 <ul>
<li>The user interacts with the command line interface and provides their desired location or query for fetching weather data.</li>
<li>The tool prompts the user for input and validates it to ensure accuracy and reliability.</li>
</ul>
</li>

<li>API Integration:
   <ul><li>The tool uses the Python requests library to make an API call to the Open Weather Map service provider.</li>
   <li> It constructs the API request URL by incorporating the user's input and any necessary parameters (e.g., API key, temperature unit). </li>
   <li>The tool sends the API request and awaits the response.</li></ul></li>

<li>Data Retrieval and Processing:
   <ul><li>Upon receiving the API response, the tool extracts the relevant weather data from the JSON or XML payload.</li>
   <li>It retrieves information such as the current temperature, weather condition, humidity, wind speed, and any other required data points.</li>  
   <li>The tool may perform data parsing, conversion, or formatting to ensure the retrieved information is in a usable format.</li>
   </ul></li>
<li>User-Friendly Display:
  <ul>
<li>The tool uses Python's PreetyTable library to create a user-friendly display for the weather data.</li>
   <li>It may utilize features such as tables, ASCII art, or formatted text to present the current weather information in a visually appealing manner.</li>
   <li>Additionally, the tool may display weather forecasts for current weather and the weather within 3hrs of interval, presenting the forecasted temperature, weather condition, and other relevant details.</li>
</ul></li>
   

<li>Error Handling:
  <ul><li>If any errors occur during the API call or data retrieval process, the tool incorporates error handling mechanisms.</li><li>It provides appropriate error messages to the user, indicating the issue encountered and providing guidance on how to resolve it.</li><li>The tool may handle various types of errors, such as network connectivity issues, invalid API responses, or incorrect user input.</li></ul></li>

<li>Command Line Arguments (Optional):
  <ul><li>The tool may support command line arguments to enhance its functionality.</li><li>Command line arguments could enable the user to specify additional options, such as choosing the temperature unit or requesting specific weather parameters to display.</li></ul></li>

<li>Documentation and Readme:
  <ul><li>The project includes comprehensive documentation and a README file to guide users on setting up, installing dependencies, and using the tool effectively.</li><li>The documentation provides clear instructions on how to interact with the command line interface, input requirements, and available functionalities.</li><li>It may include examples and sample outputs to assist users in understanding the tool's capabilities and expected results.</li></ul></li>
<li>Testing and Validation:
<ul><li>The project incorporates a testing phase to validate the tool's functionalities and ensure accurate weather data retrieval.</li><li> Test cases cover various scenarios, including both successful and error conditions, to verify that the tool behaves as expected.</li><li>Testing helps identify and address any potential issues or bugs in the implementation.</li></ul></li>
</ol>
The above architectural flow description provides an overview of the key steps involved in the Purvanuman project, from user input to displaying weather data in a user-friendly format, while incorporating error handling, command line arguments, documentation, and testing.

<br/>
<br/>
<b>Specification</b><br/>
<ul>
<li>Main Menu- On this screen, the user is greeted and a brief information about the application is given. In addition, the user is presented with options for navigation.</li>
<li>City Entry-On this screen, the user is asked to enter the name of the city for which the user wants to see the weather forecasts.</li>
 <li>Forecast Menu-On this screen, the user is presented with 3 different options. Two of them are what type of weather forecast the user wants to display, and the last one is whether the user wants to return to the main menu.
</li>
<li>Current Weather Forecast-On this screen, the current weather forecasts for the asked city are displayed in a table. Below the table, 3 different navigation options are presented to the user. According to the user's selection, the relevant screen is returned.</li>
<li>Daily Weather Forecasts at 3-hour Intervals-On this screen, daily weather forecasts are displayed at 3-hour intervals. As in the current weather forecasts screen, 3 different navigation options are presented to the user here, too.</li>
<li>Exit-This is the screen where the program is terminated. On this screen, the user is greeted and given the necessary information to re-run the application.</li>


</ul>
<br/>
<b>Future Scope</b><br/>
It will be an effective and useful option to determine the location of the user using the application and quickly show the weather forecasts for the location of the user.
The application uses the free option of OWM. Therefore, a limited number of options are offered. Offering more comprehensive weather forecasts will increase user diversity.
Showing images/emojis according to the weather conditions on the screen where the weather forecasts are displayed can make the application more attractive.
<br/>
<br/>
<b>Technologies used</b>
<br/>
Python - Used to provide the functionality of the application.
VSCode - Used to create and edit the application.
Git - Used as version control system to track changes in development process.
GitHub - Used to host the project's files and folders.
Github Copilot-GitHub Copilot is an AI pair programmer that offers autocomplete-style suggestions as you code.

<br/>
<br/>
<b>Python Libraries</b><br/>

Requests: Requests allows you to send HTTP/1.1 requests extremely easily.<br/>
secrets:secrets module is used for generating cryptographically strong random numbers suitable for managing data such as passwords, account authentication, security tokens, and related secrets<br/>
PrettyTable: A simple Python library for easily displaying tabular data in a visually appealing ASCII table format.<br/>
<br/>
<b>Installation</b><br/>
Clone this repository or download the source code / Alternatively you can run this in Github Codespaces.<br/>
Install the required libraries by running the following command: pip install -r requirements.txt<br/>
Obtain an OpenWeatherMap API key by signing up on their website.<br/>
Replace the API_KEY in secrets.ini file with your actual API key in the code.<br/>
Run main.py<br/>
project will go live<br/>


<br/><b>GitHub Copilot Assistance</b>
<br/>
API Usage: Copilot helped generate code for making API requests using the requests library. It suggests the appropriate method (get()), constructs the URL with the city name and API key, and handles HTTP errors using raise_for_status().<br/>
Data Parsing: Copilot assists with parsing the JSON response by suggesting the json() method to convert the response content to a Python dictionary. It also helps access specific weather data fields (such as weather, main, temp, and humidity) from the JSON response.<br/>
Error Handling:Copilot generates code for handling potential errors that can occur during API requests and JSON parsing. It suggests using try-except blocks to catch and handle specific exceptions (RequestException for network errors and JSONDecodeError for JSON parsing errors) and provides error messages for better error reporting.
By leveraging the capabilities of GitHub Copilot, this solution demonstrates how it can assist in writing code for API usage, data parsing, and error handling, thereby enhancing productivity and reducing manual coding efforts.
<br/><br/>
<b>Usage</b><br/>
Open a terminal or command prompt.
Navigate to the directory where the script is located.
Run the following command: python main.py
Enter the name of the city for which you want to fetch the weather forecast.
The tool will display the weather information including current weather and 3 hour weather forecast.


<b>Error Handling</b><br/>
By offering exception handling code suggestions for certain cases, GitHub Copilot additionally helped with error handling. It helped make sure the user saw the proper error messages and offered advice on how to handle API problems like unauthorised access or invalid city names.
Even though GitHub Copilot was a great help during the development process, it's crucial to check and validate the generated code to guarantee its accuracy, security, and compliance with standard coding practises. Instead than replacing thoughtful coding and code review, the tool should be utilised as an aid.

<b>Conclusion</b><br/>
GitHub Copilot greatly enhanced the development experience for the Weather Forecasting Tool by providing code suggestions and generating snippets for API usage, data parsing, and error handling. Its AI-powered assistance expedited the development process and improved overall productivity.
Please note that GitHub Copilot was used in combination with human expertise and guidance. It is essential to understand the code generated by Copilot and review it carefully to ensure it meets your project's specific requirements and standards.
