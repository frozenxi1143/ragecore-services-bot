# Ragecore Services Verify Bot

A ready-to-run Discord verification bot using your uploaded logo.

## Features
- Slash command: `/setupverify`
- Creates a verification embed with your logo
- Users click the Verify button to receive the `Verified` role
- Automatically creates the role if it does not exist

## Setup

### 1. Create a Discord Bot
Go to:
https://discord.com/developers/applications

- Create a new application
- Go to Bot
- Reset/Copy token
- Enable:
  - SERVER MEMBERS INTENT

### 2. Invite Bot
OAuth2 > URL Generator:
- scopes:
  - bot
  - applications.commands
- bot permissions:
  - Manage Roles
  - Send Messages
  - Embed Links

### 3. Install
Open terminal in the folder:

Windows:
```bash
pip install -r requirements.txt
```

### 4. Configure Token
Rename:
`.env.example` -> `.env`

Paste your token:
```env
DISCORD_TOKEN=YOUR_TOKEN
```

### 5. Run Bot
```bash
python bot.py
```

### 6. Setup Verification
In your Discord server:
```bash
/setupverify
```

The bot will post the verification panel instantly.


## One-Click Railway Deploy

1. Upload this folder to GitHub
2. Go to https://railway.app/new
3. Deploy from GitHub Repo
4. Add variable:
   DISCORD_TOKEN=YOUR_TOKEN
5. Bot starts automatically

No extra setup required.
