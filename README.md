# Flask Spotify Artist Transfer

To get started, you will need to have venv and flask installed
You will also need credentials for Spotify's API
You can get those <a href="https://developer.spotify.com/dashboard/">here</a>

Create a file called `config.py` based on the `config.template` in the root directory and fill in the client id and secret

From here, you should be able to run the app by using 

`source venv/bin/activate` to get into your virtual environment
then
`export FLASK_APP=spotifyartists.py`
to run the app

When running the app, you'll be prompted to log in first with the account you want to transfer from

Grant permissions to see your followed artists and you'll be redirected to a success page with your first token

Spotify requires that we then get another token, so press submit again and wait for a while so the app can collect all your liked artist ids

Before clicking the link to connect your second account, make sure to copy the list of comma separated IDs below the link. (Hopefully I will find a better way to do this later)

After clicking the link, you will need to grant access to modify followed artists to your second account. You will probably need to click 'Not you?' above the agree button to make sure you grant access to the account you want to transfer to.

After that you'll be redirected to another success screen with your first code. Press submit again there to get your second code and paste the ids you copied into the text box next to the submit button.

Press submit and wait while your liked artists are transferred!