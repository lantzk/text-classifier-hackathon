from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from text_classifier_api import TextInput, ClassificationResult, classify_text
from fastapi import FastAPI, Form
from typing import Annotated


from fastapi.responses import HTMLResponse, PlainTextResponse

import os

# Load environment variables
load_dotenv()

# Create FastAPI app
app = FastAPI(title="Advanced Text Classification API")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.post("/classify", response_model=ClassificationResult)
async def classify_text_endpoint(claim: Annotated[str, Form()]):
    return await classify_text(claim)

@app.get("/",response_class=HTMLResponse)
async def root():
    return '''
    <style>
:root,::backdrop{--sans-font:-apple-system,BlinkMacSystemFont,"Avenir Next",Avenir,"Nimbus Sans L",Roboto,"Noto Sans","Segoe UI",Arial,Helvetica,"Helvetica Neue",sans-serif;--mono-font:Consolas,Menlo,Monaco,"Andale Mono","Ubuntu Mono",monospace;--standard-border-radius:5px;--bg:#fff;--accent-bg:#f5f7ff;--text:#212121;--text-light:#585858;--border:#898ea4;--accent:#0d47a1;--accent-hover:#1266e2;--accent-text:var(--bg);--code:#d81b60;--preformatted:#444;--marked:#fd3;--disabled:#efefef}@media (prefers-color-scheme:dark){:root,::backdrop{color-scheme:dark;--bg:#212121;--accent-bg:#2b2b2b;--text:#dcdcdc;--text-light:#ababab;--accent:#ffb300;--accent-hover:#ffe099;--accent-text:var(--bg);--code:#f06292;--preformatted:#ccc;--disabled:#111}img,video{opacity:.8}}*,:before,:after{box-sizing:border-box}textarea,select,input,progress{-webkit-appearance:none;-moz-appearance:none;appearance:none}html{font-family:var(--sans-font);scroll-behavior:smooth}body{color:var(--text);background-color:var(--bg);grid-template-columns:1fr min(45rem,90%) 1fr;margin:0;font-size:1.15rem;line-height:1.5;display:grid}body>*{grid-column:2}body>header{background-color:var(--accent-bg);border-bottom:1px solid var(--border);text-align:center;grid-column:1/-1;padding:0 .5rem 2rem}body>header>:only-child{margin-block-start:2rem}body>header h1{max-width:1200px;margin:1rem auto}body>header p{max-width:40rem;margin:1rem auto}main{padding-top:1.5rem}body>footer{color:var(--text-light);text-align:center;border-top:1px solid var(--border);margin-top:4rem;padding:2rem 1rem 1.5rem;font-size:.9rem}h1{font-size:3rem}h2{margin-top:3rem;font-size:2.6rem}h3{margin-top:3rem;font-size:2rem}h4{font-size:1.44rem}h5{font-size:1.15rem}h6{font-size:.96rem}p{margin:1.5rem 0}p,h1,h2,h3,h4,h5,h6{overflow-wrap:break-word}h1,h2,h3{line-height:1.1}@media only screen and (width<=720px){h1{font-size:2.5rem}h2{font-size:2.1rem}h3{font-size:1.75rem}h4{font-size:1.25rem}}a,a:visited{color:var(--accent)}a:hover{text-decoration:none}button,.button,a.button,input[type=submit],input[type=reset],input[type=button],label[type=button]{border:1px solid var(--accent);background-color:var(--accent);color:var(--accent-text);padding:.5rem .9rem;line-height:normal;text-decoration:none}.button[aria-disabled=true],input:disabled,textarea:disabled,select:disabled,button[disabled]{cursor:not-allowed;background-color:var(--disabled);border-color:var(--disabled);color:var(--text-light)}input[type=range]{padding:0}abbr[title]{cursor:help;text-decoration-line:underline;text-decoration-style:dotted}button:enabled:hover,.button:not([aria-disabled=true]):hover,input[type=submit]:enabled:hover,input[type=reset]:enabled:hover,input[type=button]:enabled:hover,label[type=button]:hover{background-color:var(--accent-hover);border-color:var(--accent-hover);cursor:pointer}.button:focus-visible,button:focus-visible:where(:enabled),input:enabled:focus-visible:where([type=submit],[type=reset],[type=button]){outline:2px solid var(--accent);outline-offset:1px}header>nav{padding:1rem 0 0;font-size:1rem;line-height:2}header>nav ul,header>nav ol{flex-flow:wrap;place-content:space-around center;align-items:center;margin:0;padding:0;list-style-type:none;display:flex}header>nav ul li,header>nav ol li{display:inline-block}header>nav a,header>nav a:visited{border:1px solid var(--border);border-radius:var(--standard-border-radius);color:var(--text);margin:0 .5rem 1rem;padding:.1rem 1rem;text-decoration:none;display:inline-block}header>nav a:hover,header>nav a.current,header>nav a[aria-current=page],header>nav a[aria-current=true]{border-color:var(--accent);color:var(--accent);cursor:pointer}@media only screen and (width<=720px){header>nav a{border:none;padding:0;line-height:1;text-decoration:underline}}aside,details,pre,progress{background-color:var(--accent-bg);border:1px solid var(--border);border-radius:var(--standard-border-radius);margin-bottom:1rem}aside{float:right;width:30%;margin-inline-start:15px;padding:0 15px;font-size:1rem}[dir=rtl] aside{float:left}@media only screen and (width<=720px){aside{float:none;width:100%;margin-inline-start:0}}article,fieldset,dialog{border:1px solid var(--border);border-radius:var(--standard-border-radius);margin-bottom:1rem;padding:1rem}article h2:first-child,section h2:first-child,article h3:first-child,section h3:first-child{margin-top:1rem}section{border-top:1px solid var(--border);border-bottom:1px solid var(--border);margin:3rem 0;padding:2rem 1rem}section+section,section:first-child{border-top:0;padding-top:0}section+section{margin-top:0}section:last-child{border-bottom:0;padding-bottom:0}details{padding:.7rem 1rem}summary{cursor:pointer;word-break:break-all;margin:-.7rem -1rem;padding:.7rem 1rem;font-weight:700}details[open]>summary+*{margin-top:0}details[open]>summary{margin-bottom:.5rem}details[open]>:last-child{margin-bottom:0}table{border-collapse:collapse;margin:1.5rem 0}figure>table{width:max-content;margin:0}td,th{border:1px solid var(--border);text-align:start;padding:.5rem}th{background-color:var(--accent-bg);font-weight:700}tr:nth-child(2n){background-color:var(--accent-bg)}table caption{margin-bottom:.5rem;font-weight:700}textarea,select,input,button,.button{font-size:inherit;border-radius:var(--standard-border-radius);box-shadow:none;max-width:100%;margin-bottom:.5rem;padding:.5rem;font-family:inherit;display:inline-block}textarea,select,input{color:var(--text);background-color:var(--bg);border:1px solid var(--border)}label{display:block}textarea:not([cols]){width:100%}select:not([multiple]){background-image:linear-gradient(45deg,transparent 49%,var(--text)51%),linear-gradient(135deg,var(--text)51%,transparent 49%);background-position:calc(100% - 15px),calc(100% - 10px);background-repeat:no-repeat;background-size:5px 5px,5px 5px;padding-inline-end:25px}[dir=rtl] select:not([multiple]){background-position:10px,15px}input[type=checkbox],input[type=radio]{vertical-align:middle;width:min-content;position:relative}input[type=checkbox]+label,input[type=radio]+label{display:inline-block}input[type=radio]{border-radius:100%}input[type=checkbox]:checked,input[type=radio]:checked{background-color:var(--accent)}input[type=checkbox]:checked:after{content:" ";border-right:solid var(--bg).08em;border-bottom:solid var(--bg).08em;background-color:#0000;border-radius:0;width:.18em;height:.32em;font-size:1.8em;position:absolute;top:.05em;left:.17em;transform:rotate(45deg)}input[type=radio]:checked:after{content:" ";background-color:var(--bg);border-radius:100%;width:.25em;height:.25em;font-size:32px;position:absolute;top:.125em;left:.125em}@media only screen and (width<=720px){textarea,select,input{width:100%}}input[type=color]{height:2.5rem;padding:.2rem}input[type=file]{border:0}hr{background:var(--border);border:none;height:1px;margin:1rem auto}mark{border-radius:var(--standard-border-radius);background-color:var(--marked);color:#000;padding:2px 5px}mark a{color:#0d47a1}img,video{border-radius:var(--standard-border-radius);max-width:100%;height:auto}figure{margin:0;display:block;overflow-x:auto}figure>img,figure>picture>img{margin-inline:auto;display:block}figcaption{text-align:center;color:var(--text-light);margin-block:1rem;font-size:.9rem}blockquote{border-inline-start:.35rem solid var(--accent);color:var(--text-light);margin-block:2rem;margin-inline:2rem 0;padding:.4rem .8rem;font-style:italic}cite{color:var(--text-light);font-size:.9rem;font-style:normal}dt{color:var(--text-light)}code,pre,pre span,kbd,samp{font-family:var(--mono-font);color:var(--code)}kbd{color:var(--preformatted);border:1px solid var(--preformatted);border-bottom:3px solid var(--preformatted);border-radius:var(--standard-border-radius);padding:.1rem .4rem}pre{color:var(--preformatted);max-width:100%;padding:1rem 1.4rem;overflow:auto}pre code{color:var(--preformatted);background:0 0;margin:0;padding:0}progress{width:100%}progress:indeterminate{background-color:var(--accent-bg)}progress::-webkit-progress-bar{border-radius:var(--standard-border-radius);background-color:var(--accent-bg)}progress::-webkit-progress-value{border-radius:var(--standard-border-radius);background-color:var(--accent)}progress::-moz-progress-bar{border-radius:var(--standard-border-radius);background-color:var(--accent);transition-property:width;transition-duration:.3s}progress:indeterminate::-moz-progress-bar{background-color:var(--accent-bg)}dialog{max-width:40rem;margin:auto}dialog::backdrop{background-color:var(--bg);opacity:.8}@media only screen and (width<=720px){dialog{max-width:100%;margin:auto 1em}}sup,sub{vertical-align:baseline;position:relative}sup{top:-.4em}sub{top:.3em}.notice{background:var(--accent-bg);border:2px solid var(--border);border-radius:var(--standard-border-radius);margin:2rem 0;padding:1.5rem}
    </style>
<form id="classify" action="/classify" method="post" id="classify">
<label for="claim">Claim:</label>

<textarea id="claim" name ="claim">
</textarea>

<button type="submit" form="classify" value="Submit">Submit</button>
</form>
'''

@app.get("/about")
async def about():
    return {
        "info": "This is an advanced text classification API using the Groq API to analyze text for factuality and bias."
    }

# Add these lines at the end of the file
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
