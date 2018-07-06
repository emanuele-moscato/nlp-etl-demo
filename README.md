# Twitter scraping and sentiment analysis pipeline

In this demo we call the Twitter API to get the tweets from @bbc and perform sentiment analysis on the texts, creating a pipeline scheduled to run every hour with cron.

Just run `/scripts/pipeline.sh` by itself or as a cron job and run the app: the pipeline downloads the tweets from the @bbc account puts them in the `input/` folder, uses `babylon` to perform sentiment analysis and then puts the results in the `output/` folder. The app then reads the results and serves them in a table.

Requirements:
- [`babylon`](https://bitbucket.org/theasi/alexandria-babylon/src/master/)
- `tqdm` because it's cool (to install: `pip install tqdm`)