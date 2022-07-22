# SkyKings Translations

Translations for the SkyKings Discord bot.

## Translating the bot

**You must have a GitHub account to submit translations. Create one [here](https://github.com/signup).**

Before translating the bot, we ask that you:
- Are fluent in the English language.
- Are fluent in whatever language you are translating to.

To start, first pick a language. 

Because of how Discord works, we are limited to the languages listed [here](https://discord.com/developers/docs/reference#locales).

Once you have picked a language, click the `Fork` button in the top right to make a copy of this repository.
![image](https://user-images.githubusercontent.com/49261529/180373224-1e582f8d-923a-4b3d-89c0-d41bf2381829.png)

After you have forked the repository, you will be brought to your copy, or 'fork', of it.

Create a file under the `translations` directory titled `locale.json`, `locale` being the locale of the language you chose. (e.g. `en-US`)

Now, in that same directory, copy `en-US.json` into your new file and translate the text in it.

When translating, **DO NOT** translate:
- The JSON keys.
    - Only translate strings after the colon (`:`).
- Things surrounded in curly brackets (`{}`).
    - These are variables the bot uses to format the text it sends.
- Things that aren't translated in Hypixel (e.g. if a skill name isn't translated on Hypixel, don't translate it here).
- Markdown.
    - Typically things surrounded in arrows (`<>`) or special characters for formatting the output, such as \*, \`, and \_.
    
## Submitting the translation

To submit the translation, navigate to the [`Pull Requests` tab](https://github.com/SkyKings-Guild/translations/pulls) and click `New Pull Request`.
![image](https://user-images.githubusercontent.com/49261529/180374143-8bf78d31-0511-4ec5-b7fd-4628b2733874.png)

Fill out the template, and then click `Create Pull Request`.
