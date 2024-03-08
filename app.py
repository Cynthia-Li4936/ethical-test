{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a99b93c2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app '__main__'\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.\n",
      " * Running on http://127.0.0.1:5000\n",
      "Press CTRL+C to quit\n",
      "127.0.0.1 - - [08/Mar/2024 20:35:02] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [08/Mar/2024 20:35:13] \"GET / HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [08/Mar/2024 20:35:22] \"POST /main HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [08/Mar/2024 20:35:26] \"POST /ethical_test HTTP/1.1\" 200 -\n",
      "127.0.0.1 - - [08/Mar/2024 20:35:31] \"POST /answer HTTP/1.1\" 404 -\n"
     ]
    }
   ],
   "source": [
    "from flask import Flask, request, render_template\n",
    "\n",
    "app = Flask(__name__)\n",
    "\n",
    "@app.route(\"/\", methods = [\"GET\", \"POST\"])\n",
    "def index():\n",
    "    return(render_template(\"index.html\"))\n",
    "\n",
    "@app.route(\"/main\", methods = [\"GET\", \"POST\"])\n",
    "def main():\n",
    "    name = request.form.get(\"name\")\n",
    "    return(render_template(\"main.html\", name=name))\n",
    "\n",
    "@app.route(\"/ethical_test\", methods = [\"GET\", \"POST\"])\n",
    "def ethical_test():\n",
    "    return(render_template(\"ethical_test.html\"))\n",
    "\n",
    "@app.route(\"/end\", methods = [\"GET\", \"POST\"])\n",
    "def end():\n",
    "    return(render_template(\"end.html\"))\n",
    "\n",
    "\n",
    "if __name__ == \"__main__\":\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "46f26d4d",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5207417b",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
