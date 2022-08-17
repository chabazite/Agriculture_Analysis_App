# Link to Webapp: <a href="https://agricultural-analysis.herokuapp.com/" target="_blank">World Agricultural Dashboard</a>
# Agriculture Analysis Dashboard
==============================

## Business Case
<a name="Business_Case"></a>

As the population on earth continues to grow, so too does the demand placed on the agricultural industry. 

Our society has always grown at the hands of improvements to this industry. There have been three major agricultural revolutions throughout human history. With each, comes a drastic increase in humanity ability to sustain larger populations. 

 **Neolithic Revolution** <br>
The first revolution saw humans transition from a hunter-gatherer species, to one of organized communities and agriculture. While many improvements such as irrigation came at this early stage, the domestication and selective breeding of cereal grasses set the stage for agriculture as we know it today. 

**British Agricultural Revolution**<br>
While this time period is dominated by the onset of the industrial revolution, the second agricultural revolution has been cited as the cause for this drastic shift in society. Again main advancement through the british agricultural and industrial revolution propelled humanity into another great population boon. Many historians credit one of the most important advancement to be the Norfolk four-course rotation. This new stype of crop rotation, increased soil fertility through the use of nitrogen-fixing clover, as well as providing winter turnips, which utilized deeper soil nutrients due to its root structure. It’s possible this increase in productivity for both crops and workers is what allowed for the industrial revolution to boom.

**Green Revolution**<br>
Starting in the 50s and 60s, the third great agricultural revolution began. This revolution had widespread impact on a reduction in land use, poverty, worldwide hunger, and even infant mortality. This was due to advancements across the board in agricultural chemical use including pesticides and fertilizers, high yield seeds, and the introduction to modern machineries. 

While these revolutions have paved the way for our population growth, none of them were without their pain points and each of them have successively led to an reduction in finite resources of our earth. 

How has the Green Revolution changed humanity and the way we steward our limited and ultimate resource of land?

1. What kind of change has the world seen in population?
2. How has land development changed?
3. How has Agriculture demand and economics changed? 
4. How have major world issues been impacted?

## Table of Contents
<details open>
  <summary>Show/Hide</summary>
  <br>
 
1. [ File Descriptions ](#File_Description)
2. [ Technologies Used ](#Technologies_Used)    
3. [ Structure ](#Structure)
4. [ Evaluation ](#Evaluation)
5. [ Future Improvements ](#Future_Improvements)

</details>


## Project Organization

<details>
<a name="File_Description"></a>
<summary>Show/Hide</summary>
 <br>


    ├── LICENSE
    ├── .gitignore
    ├── README.md          <- The top-level README for developers using this project.
    │
    ├── agenv                <- Virtual Environment for the project
    │
    ├── dashboard_app      <- Folder that contains all deployment needs
    │   ├── images         <- directory of images for the app
    │   ├── templates      <- html webpages
    │       ├── index.html    <- 
    │       └──               <- 
    │   ├── __init__.py    <- 
    │   ├── routes.py      <- 
    │   └──                <- 
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    └── setup.py           <- makes project pip installable (pip install -e .) so src can be imported 

--------
  </details>   

## Technologies Used:
<details>
<a name="Technologies_Used"></a>
<summary>Show/Hide</summary>
<br>

      
    ├──Heroku
    ├──Python
        ├──Numpy
        ├──Pandas
        ├──Flask
        ├──aiosync
        ├──Matplotlib
        ├──Seaborn
        ├──aiohttp
        └──plotly
 
 ------------
 </details>

## Structure of Notebooks:
<details>
<a name="Structure"></a>
<summary>Show/Hide</summary>
<br>

 1. API Practice
      * 1.0 Learning how to utilize the Worldbank API
 2. API Data Wrangling
      * 2.0 Indicators and Requests
      * 2.1 Combining Dataframes
      * 2.2 Top 10 vs. Other Country Dataframe

 3. Exploratory Data Analysis
      * 3.0 Importing
      * 3.1 Question 1: Population
      * 3.2 Question 2: Land Development
      * 3.4 Question 3: Agricultural Practices
      * 3.5 Question 4: World Issues
     

 </details>

## Evaluation:
<a name="Evaluation"></a>
<details>
<summary>Show/Hide</summary>
<br>
      * Question 1: Population
          It is interesting to note that around 2007 the world population for rural inhabitats begin to slow and then stop entirely, while urban population continues to climb. When breaking this down by country it is easy to see the biggest impact here is China.

      * Question 2: Land Development
          

      * Question 3: Agricultural Practices


      * Question 4: World Issues
          It is clear that Greenhouse Gases are still going up at a steep rate. There also appears to be a releationship between poverty and mortality under 5, which is expected. Both have gone down since 1990s. 



 Here is a link to the <a href="https://agricultural-analysis.herokuapp.com/" target="_blank">app</a>. 

</details>
  
## Future Improvements
 <a name="Future_Improvements"></a>
 <details>
<summary>Show/Hide</summary>
<br>
 One of the biggest issues with this project is currently load times of the deployment. I was able to bring down the load times using async requests for the APIs, but 12 seconds to load is still way too long. I will also place time into documenting the questions each page is trying to answer in order to make the user's experience more streamlined.

</details>

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
<p>README outline tailored from [awesomeahi95][]<p>
