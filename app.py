import pandas as pd
import plotly.express as px
import requests
from bs4 import BeautifulSoup
import streamlit as st


def request_github_trending(url):
    """
        this function sends a get request
        to the website and get its response.

        parameters :
            url : url of the website

        returns :
            response of the get request of the
            url.

    """

    # send a get request and get the response
    response = requests.get(url)

    # return the response
    return response


def extract(page):
    """
        this function gets information of
        trending repos in the GitHub.

        parameters :
            page : 	response of the get request to the
                GitHub page

        returns :
            html code corresponding to all the rows
            which are related to each repository.

    """

    # make a beautifulsoup object using the html of the page
    doc = BeautifulSoup(page.text, "html.parser")

    # getting all rows related to repositories
    repo_info = doc.find_all("article")

    # return repositories
    return repo_info


def transform(html_repos):
    """
            this function makes a hash using repository information.
            parameters :
                html_repos	:	html code related to repository information rows.
            returns :
                list of hash in the format of
                {
                    developer : "Developer",
                    name of repository : "Name of repository",
                    stars : "Stars"
                }
                    related to all the repositories
    """
    result = []
    for row in html_repos:
        REPOSITORY_NAME = ''.join(row.select_one('h2.h3.lh-condensed').text.split()).split('/')[1]
        NBR_STARS = ' '.join(row.select_one('a.Link--muted.d-inline-block.mr-3').text.split())

        try:
            NAME = row.select_one('img.avatar.mb-1.avatar-user')['alt']
        except:
            NAME = "hidden_name"
        result.append({'Developer': NAME, 'Repository name': REPOSITORY_NAME, 'NBR stars': NBR_STARS})
    return result


def load_data(data):
    """
            this function constructs DataFrame from a list.
            parameters:
                data : list of hash related to all the repositories
            returns : Ordered data frames

    """
    df = pd.DataFrame(data)
    df['NBR stars'] = df['NBR stars'].apply(lambda x: int(x.replace(',', '')))
    df.sort_values(by='NBR stars', inplace=True, ascending=True)
    df.reset_index(inplace=True)
    df.drop('index', axis=1, inplace=True)
    return df


def data_visual(df):
    fig = px.bar(df, x='NBR stars', y="Repository name",
                 color='NBR stars', orientation='h',
                 width=1500, height=800)
    fig.update_layout(
        xaxis_title="Stars",
        yaxis_title="Repository name",
        legend_title="NBR stars",
        title={
            'text': 'See what the GitHub community is most excited about today',
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
        },

        font=dict(
            size=16,
        ))
    return fig


def _main():
    # URL of the website
    URL = "https://github.com/trending"

    # get the response
    page = request_github_trending(URL)

    # get the html code related to repo rows
    repo_info = extract(page)

    # get the hash list related to repo rows
    transformed_repo_info = transform(repo_info)

    dataset = load_data(transformed_repo_info)

    data_vs = data_visual(dataset)

    return data_vs


_main()


def main_page():
    st.set_page_config(layout="wide")
    st.markdown(""" 
       <nav class="navbar navbar-expand-lg navbar-dark" class="navbar navbar-dark bg-dark" style="background-color: #3498DB;">
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarTogglerDemo01" aria-controls="navbarTogglerDemo01" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarTogglerDemo01">
        <a class="navbar-brand" href="https://github.com/abdullaabdukulov"; return false;" class="text-dark">Developer</a>
        <ul class="navbar-nav mr-auto mt-2 mt-lg-0">
          <li class="nav-item active">
            <a class="navbar-brand" class="text-primary" href="https://github.com/trending">Trending <span class="sr-only">(current)</span></a>
          </li>
        </ul>
      </div>
    </nav>
        """, unsafe_allow_html=True)
    st.markdown("<h1 style='width: 500px; margin: auto; border: 3px; text-align: left; flex: 0'>Trending</h1>",
                unsafe_allow_html=True)
    st.markdown("""<style>
    .css-k1vhr4
    {
    display: block;
    margin: 60px;
    }
    .css-hxt7ib {
    padding-top: 2rem;
    padding-left: 1rem;
    padding-right: 1rem;
}
    .css-hxt7ib h1 {
    font-size: 2.5rem;
    font-weight: 600;
}
                </style>""", unsafe_allow_html=True)
    left, middle, right = st.columns((2, 5, 2))
    with left:
        st.plotly_chart(_main(), use_container_width=False)
    st.markdown(
        '<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">',
        unsafe_allow_html=True)


main_page()
