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
    ├── agenv              <- Virtual Environment for the project
    │
    ├── web_app            <- Folder that contains all deployment needs
    │   ├── dashboard_app       
    │   │      ├── statics                  <- directory of images for the app
    │   │      │    ├── githublogo.png            <- github logo 
    │   │      │    ├── linkedinlogo.png          <- linkedin logo
    │   │      │    └── mediumlogo.png            <- medium logo
    │   │      ├── templates                <- html folder structure
    │   │      │    ├── base.html                 <- basic structure for all html templates
    │   │      │    ├── economics.html            <- economics page
    │   │      │    ├── filter_dropdown.html      <- abstracted filter dropdown item for all html pages
    │   │      │    ├── global_issues.html        <- global issue page
    │   │      │    ├── index.html                <- index home page
    │   │      │    ├── land_use.html             <- land use page
    │   │      │    ├── nav.html                  <- abstracted navigation bar
    │   │      │    ├── population.html           <- population page  
    │   │      │    └── sidebar.html              <- abstracted sidebar item
    │   │      ├── __init__.py              <- import Flask from Flask and set app name
    │   │      └── routes.py                <- routes all the pages for the flask app
    │   ├── scripts          
    │   │      ├── __init__.py              <- allows importation of scripts
    │   │      ├── additional_features.py   <- contains extract calculation functions for each page
    │   │      ├── dataframe_compile.py     <- contains functions for all dataframe wrangling
    │   │      ├── economics_data.py        <- function for economics page graphs
    │   │      ├── home_data.py             <- function for main page graph
    │   │      ├── issues_data.py           <- function for global issues page graphs
    │   │      ├── population_data.py       <- function for population page graphs           
    │   │      └── top_10_calc.py           <- functions for the filter dropdown
    │   ├── requirements.txt            <- The requirements file for reproducing the analysis environment, generated with `pip freeze > requirements.txt`
    │   ├── Procfile                    <- a file that specifies the commands that are executed. by an Heroku app on startup
    │   └── app.py                      <- serves the app
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    └── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
        └── figures        <- Generated graphics and figures to be used in reporting
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
      * 2.2 Top 10 vs. Other Country Dataframes
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

These are just a few insights from the analysis:

* Question 1: Population
   * It is interesting to note that around 2007 the world population for rural inhabitats begin to slow and then almost stop entirely, while urban population continues to climb. When breaking this down by country it is easy to see the biggest impact here is China, which began to lose rural population since 1992. We can also see that China and India are the two outlier countries when it comes to populations. This causes the Top 10 largest countries in populations to have a larger combined population than the rest of the world's countries combined.

* Question 2: Land Development
   * Interesting that Indonesia has a lot of crop land, but very little arable land. The Top 10 largest countries are mainly arable land, while the other nations are mainly crop land. Agricultural land per person has also been decreasing. This makes sense, there isn't much increase in actual agricultural land, but population is moving up at an increasing pace. Finally, cereal land use has been increasing over time, this makes sense considering the importance of these grains in human and livestock nutrition.

* Question 3: Agricultural Practices
   * There is clearly an increase in fertilizer use. This makes sense considering the green revolution's focus was on the advent of chemical fertilizers. There is also a linear relationship for the use of fertilizer with increase in cereal grain yield. There is an interesting relationship between GDP, fertilizer Use, and cereal grain yield. The Top_10 group has a consistant GDP for their goods, whereas the Other nations vary from very high to a large grouping of very low GDP. This makes sense considering many developing nations will utilize their own crops within household.

* Question 4: World Issues
   * It is clear that Greenhouse Gases are still going up at a steep rate. There also appears to be a relationship between poverty and mortality under 5, which is expected. When looking at the top 10 most populated countries vs all other nations, there is a clear clustering for poverty vs. rural. Top 10 nations have low poverty and high rural population, while other nations have higher poverty and lower rural population. Additionally, between the two there are two clusters with mortality and poverty, with the top 10 nations having lower poverty and slightly larger range of mortality under 5, vs. the other nations that have higher average mortality rates under five and higher poverty rates. The good news is both groups have decreased in mortality rates since 1960.  



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
