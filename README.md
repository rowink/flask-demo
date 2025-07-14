# Vercel Flask Demo

This project demonstrates how to deploy a simple Flask web application on [Vercel](https://vercel.com/). It provides an example of integrating a Python backend with Vercel’s serverless platform, enabling fast and scalable deployments.

## Features

- Minimal Flask app with a sample route (`/`)
- Vercel configuration for seamless deployment
- Quick start instructions
- Easily customizable for your own API endpoints

## Getting Started

1. **Clone this repository**

   ```bash
   git clone https://github.com/rowink/flask-demo.git
   cd flask-demo
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**

   ```bash
   cd api
   flask run
   ```

   By default, Flask will serve at `http://127.0.0.1:5000/`.

4. **Deploy to Vercel**

   Click the button below to deploy your own copy to Vercel:

   [![Deploy to Vercel](https://vercel.com/button)](https://vercel.com/import/project?template=https://github.com/rowink/flask-demo)

   Or, from the command line, if you have [Vercel CLI](https://vercel.com/docs/cli):

   ```bash
   vercel
   ```

## Customizing Your Flask App

- Modify `api/index.py` to add or change routes.
- Install additional Python packages as needed by adding them to `requirements.txt`.

## Notes

- The Flask app **must** reside inside the `api/` directory for Vercel’s Python runtime to detect it properly.
- On Vercel, each request spins up a new serverless function instance, so avoid using global state.
- For more advanced configuration, edit `vercel.json` as needed.

## References

- [Flask documentation](https://flask.palletsprojects.com/)
- [Vercel Python documentation](https://vercel.com/docs/runtimes#official-runtimes/python)
- [Vercel CLI](https://vercel.com/docs/cli)

---

Happy deploying! 🚀
