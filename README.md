

## Developer Note

- __This repository is not intended or supported for deployment on KOYEB.__
- If Hosted On Heroku Then Make Sure You Are Using Premium Dynos Or Any Above then basic dynos.
- If You Don't Have High End VPS like 8vcpu or 32GiB RAM So Don't Deploy This Bot.
- You Can Customize FFMPEG Code If You Know What You Are Doing.
- __Ensure that you have adhered to this developer note before reporting any errors.__

## Changelog Of Latest Update

### v0.0.8
- Shifted To Mongo Database.
- Changed Hashing Algo To SHA256.
- Added About Command.

### v0.0.7
- Added Separate Anime Channel Upload
- <details><summary>Click Here To See How Separate Anime Channel Upload Look.</summary><img src="https://graph.org/file/a0636332545730a4d3d43.jpg" alt="sepul1"/><img src="https://graph.org/file/3eb0b86609469f385f4b5.jpg" alt="sepul2"/></details>
- Added Button Upload Support (File Store)
- <details><summary>Click Here To See How Button Upload Look.</summary><img src="https://graph.org/file/3e9abc9ec7de6a26fd1a1.jpg" alt="btnul"/></details>
- Added Multi Thread Encoding
- Added Progress Bar of Encoding
- Added Option For Logs In Main Channel
- Added ForceSub
- Added 480p Support
- Added Broadcast
- Major Modification In FFMPEG Code.
- Modified Anime Searcher
- Admin Panel Fixed
- ReWritten Whole Program (Fully OOPs Based)
- Optimized Core
- Added Heroku Support
- Added Custom CRF Support

## Contributing

- Any Sort of Contributions are Welcomed!
- Try To Resove Any Task From ToDo List Or Raise A Issue!


### Fork Repo Then click on below button of ur fork repo.
[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

## Developer Note

- If Hosted On Heroku Then Encoding Of Per Episode Will Take Around 20mins.
- If You Don't Have High End VPS like 8vcpu or 32GiB RAM So Don't Deploy This Bot.
- You Can Customize FFMPEG Code If You Know What You Are Doing.

## Environmental Variable

### REQUIRED VARIABLES

- `BOT_TOKEN` - Get This From @Botfather In Telegram.

- `MONGO_SRV` - Get This From mongodb.com .

- `MAIN_CHANNEL` - ID of Channel Where Anime Will Upload.

- `CLOUD_CHANNEL` - ID of Channel Where Samples And Screenshots Of Anime Will Be Uploaded.

- `LOG_CHANNEL` - ID of Channel Where Status Of Proccesses Will Be Shown.

- `OWNER` - ID of Owner.

### OPTIONAL VARIABLES

- `SESSION` - Telethon Session String Of Your Telegram Account.

- `BACKUP_CHANNEL` - ID of Channel Where Anime Will Be Saved As BackUP if You Are Using Button Upload Option Then Make Sure To SET Backup Channel.

- `FORCESUB_CHANNEL` - ID of Channel Where You Want The User To Join (Make Sure You Promoted The Bot in that channel).

- `FORCESUB_CHANNEL_LINK` - Link of Channel Via User Join The `FORCESUB_CHANNEL`.

- `THUMBNAIL` - JPG/PNG Link of Thumbnail FIle.

- `FFMPEG` - You Can Set Custom Path Of ffmpeg if u want, default is `ffmpeg`.

- `LOG_ON_MAIN` - `True/False` It Will Send LOGS in `MAIN_CHANNEL` rather than `LOG_CHANNEL`, default is `False`

- `SEND_SCHEDULE` - `True/False` Send Schedule of Upcoming Anime of that day at 00:30 **IST**, default is `False`.

- `RESTART_EVERDAY` - `True/False` It Will Restart The Bot Everyday At 00:30 **IST**, default is `True`.

- `CRF` - Less CRF == High Quality, More Size , More CRF == Low Quality, Less Size, CRF Range = 20-51.

## Deployment In VPS

- `git clone https://github.com/kaif-00z/AutoAnimeBot.git`

- `nano .env` configure env as per [this](https://github.com/kaif-00z/AutoAnimeBot/blob/main/.sample.env) or  using [this](https://github.com/kaif-00z/AutoAnimeBot/blob/main/auto_env_gen.py).

- `sudo docker build . -t ongoing` (make sure to install docker first using `sudo apt install docker.io`)

- `sudo docker run ongoing`

## Commands

![Comand](https://graph.org/file/ca8de14ba0b1d3b71af1f.jpg)


## Donate

- [Contact me on Telegram](t.me/r4h4t_69) if you would like to donate me for my work!