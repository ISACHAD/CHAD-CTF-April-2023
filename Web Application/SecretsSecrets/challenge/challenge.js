const crypto = require('crypto');
const express = require('express');
const app = express();

const notes = new Map();
const add = (note) => {
    const id = crypto
        .randomBytes(32)
        .toString('hex')

    notes.set(id, note);
    return id;
}

app.use(require('body-parser').urlencoded({ extended: false }));

app.get('/', (_req, res) => {
    res.type('html')
    res.end(`
        <link rel="stylesheet" href="/style.css" />
        <div class="container">
            <h1>Secret Posts Are So Much Fun!</h1>
            <form method="POST" action="/new">
                <input type="text" class="note" name="note" placeholder="Note" />
                <input type="submit" class="submit" value="Submit" />
            </form>
        </div>
    `);
});

app.post('/new', (req, res) => {
    const note = (req.body.note ?? '').toString();
    const id = add(note);
    res.redirect(`/view/${id}`);
});

app.get('/view/:id', (req, res) => {
    const id = req.params.id;
    res.type('html');

    if (notes.has(id)) {
        res.end(`
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>Note</h1>
                <div class="content">
                    Secret note is hidden
                </div>
                <br />
                <button class="reveal">Reveal</button>
                <a class=".prev">Previous secret note</a>
            </div>
            <script>
                const button = document.querySelector('button');
                const content = document.querySelector('.content');
                button.addEventListener('click', () => {
                    content.textContent = "${notes.get(id)}";
                    button.remove();
                });

                const previous = localStorage.previous;
                const current = window.location.toString();

                const a = document.querySelector('a');
                if (previous) {
                    a.href = previous;
                } else {
                    a.remove()
                }
                localStorage.previous = current;
            </script>
        `);
    } else {
        res.end(`
            <link rel="stylesheet" href="/style.css" />
            <div class="container">
                <h1>Secret Note</h1>
                Secret note does not exist!
            </div>
        `);
    }
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

console.log("Started challenge service");
if (process.env.CHALLENGE_PORT){
    app.listen(parseInt(process.env.CHALLENGE_PORT));
}
else {
    app.listen(3000);
}
