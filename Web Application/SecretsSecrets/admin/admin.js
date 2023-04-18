/**
 * HINT: This file is not really that important for the challenge
 * it is just here to give you context how the admin checker works.
 */

const crypto = require('crypto');
const express = require('express');
const puppeteer = require('puppeteer');
const url = require('url');
const app = express();


const challengeUrl = `https://chadctf-web-hard-secrets.chals.io`;

app.use(require('body-parser').urlencoded({ extended: false }));

const sleep = (ms) => {
    return new Promise((resolve) => {
        setTimeout(resolve, ms);
    });
}

app.get('/', (_req, res) => {
    res.type('html')
    res.end(`
        <link rel="stylesheet" href="/style.css" />
        <div class="container">
            <h1>Admin will visit the link below</h1>
            <p>Please use ${challengeUrl} as URI for below</p>
            <form method="POST" action="/visit">
                <input type="text" name="note" placeholder="URL" />
                <input type="submit" value="Submit" />
            </form>
        </div>
    `);
});

const visitUrl = (url) => {
    (async () => {
        let browser = null;
        console.log("Hello");
        if (process.env.IS_DOCKER) {
            browser = await puppeteer.launch({
                executablePath: '/usr/bin/google-chrome',
                args: ['--no-sandbox', '--disable-setuid-sandbox', '--disable-gpu']
            });
        } else {
            browser = await puppeteer.launch();
        }
        const page = await browser.newPage();
        await page.setDefaultNavigationTimeout(1000);

        const admin_port = process.env.CHALLENGE_PORT;
        await page.goto(challengeUrl);
        console.log("Went to page for flag creation");

        await page.setViewport({width: 1080, height: 1024});

        await page.type('.note', process.env.FLAG ?? 'flag missing!');
        
        // Wait and click on first result
        const submitSelector = '.submit';
        await page.waitForSelector(submitSelector);
        await page.click(submitSelector);

        const flagPost = await page.waitForSelector(".content");
        await flagPost.evaluate(el => el.textContent);

        const userUrl = new URL(url);
        const challUrl = new URL(challengeUrl);
        if (userUrl.hostname.localeCompare(challUrl.hostname) == 0)
        {
            await page.goto(url);
            await sleep(1000);

            await page.setViewport({width: 1080, height: 1024});

            await page.evaluate(() => document.querySelector('*').outerHTML);
        } else {
            console.log("Not valid id address");
        }

        await browser.close();
    })();
}

app.post('/visit', (req, res) => {
    console.log(req.body);
    const urlstr = (req.body.note ?? '').toString();
    try {
        const url = new URL(urlstr);
        visitUrl(url);
    } catch (_) { }
    res.redirect('/');
});

app.get('/style.css', (_req, res) => {
    res.end(`
        * {
            font-family: 'Helvetica Neue', sans-serif;
            box-sizing: border-box;
        }

        html, body { margin: 0; }

        .container {
            padding: 2rem;
            width: 90%;
            max-width: 900px;
            margin: auto;
        }

        input:not([type="submit"]) {
            width: 100%;
            padding: 8px;
            margin: 8px 0;
        }
    `);
});

console.log("Started admin service");
if (process.env.ADMIN_PORT){
    app.listen(parseInt(process.env.ADMIN_PORT));
}
else {
    app.listen(3001);
}
