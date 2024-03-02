# Discord Reminder Bot

This Discord bot allows users to schedule reminders for events on specific dates and times.

## Features

- Schedule reminders for events by specifying the date, time, and reminder message.
- Supports reminders for future events.

## Usage

### Prerequisites

- Python 3.x installed on your system.
- Discord account with a registered bot application.

### Installation

1. Clone or download the repository to your local machine:

   ```
   git clone https://github.com/kllarena07/ClubRemind.git
   ```

2. Install the required Python packages:

   ```
   pip install -r requirements.txt
   ```

### Configuration

1. Create a Discord bot application and obtain the bot token.
2. Rename the `.env.example` file to `.env` and update the `DISCORD_BOT_TOKEN` variable with your bot token.

### Running the Bot

Run the following command in your terminal to start the bot:

```
python bot.py
```

### Commands

- **Schedule Reminder**

  ```
  $create_event <date> <time> <reminder_message>
  ```

  Example:

  ```
  $create_event 2024-03-05 12:00 "Don't forget the meeting!"
  ```

  This command schedules a reminder for March 5th, 2024, at 12:00 PM with the message "Don't forget the meeting!".
