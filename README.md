# Welcome to My First Scraper
***

# Introduction

<img width="495" alt="meme_scraping" src="https://user-images.githubusercontent.com/95611906/200126969-42bdcb8b-b0ab-4a29-9fb2-d21a3bc5d2f2.png">


<a href="https://github.com/trending">Github trending's page</a>

<h2>Technical specifications</h2>
<p>Using python libraries <code>requests and beautifulsoup4</code>, return a CSV of the TOP 25 trending repositories from Github.</p>
<ol start="0">
<li>Request (with request)</li>
<li>Extract (with beautifulsoup4)</li>
<li>Transform</li>
<li>Format</li>
</ol>

<p><strong>Part 0: Request</strong>
Write a function prototyped: <code>def request_github_trending(url)</code> it will return the result of <code>Request</code>.</p>
<p><strong>Part 1: Extract</strong>
Write a function prototyped: <code>def extract(page)</code> to <code>find_all</code> instances of HTML code of repository rows and return it. You should use <code>BeautifulSoup</code>. :-)</p>
<p><strong>Part 2: Transform</strong>
Write a function prototyped: <code>def transform(html_repos)</code> taking an array of all the instances of HTML code of the repository row.
It will return an array of hash following this format: <code>[{'developer': NAME, 'repository_name': REPOS_NAME, 'nbr_stars': NBR_STARS}, ...]</code></p>
<p><strong>Part 3: Format</strong>
Write a function prototyped: <code>def format(repositories_data)</code> taking a repository array of hash and transforming it and returning it into a <code>CSV</code> string. Each column will be separated by <code>,</code> and each line by <code>\n</code>
The columns will be <code>Developer</code>,<code>Repository Name</code>,<code>Number of Stars</code></p>



<img width="2048" alt="image" src="https://user-images.githubusercontent.com/95611906/200127918-5fc0946a-1eed-4b6f-9a64-a285c799187f.png">
<a href="https://abdullaabdukulov-my-first-scraper-app-1p3avr.streamlit.app/">Demo version</a>
