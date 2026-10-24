import os, datetime
DOMAIN = "https://sizetrim.co.uk"      # <- change to your real domain, then run: python3 build.py
SITE = "SizeTrim"                    # <- change to your brand name
ADSENSE_CLIENT = ""                    # <- e.g. "ca-pub-1234567890123456" after AdSense approval
AD_SLOT = ""                           # <- your ad unit slot id

def lab(n): return f"{n//1024}MB" if n >= 1024 else f"{n}KB"
pages = []  # (slug, title, h1, desc, mode, target, intro, tips)

img_sizes = [10,15,20,25,30,40,50,70,100,150,200,300,500]
for n in img_sizes:
    pages.append((f"compress-image-to-{n}kb", f"Compress Image to {n}KB – Free Online Image Reducer",
      f"Compress Image to {n}KB", f"Reduce any JPG, PNG or WebP photo to under {n}KB for free. Private, runs in your browser.",
      "image", n,
      f"Need your photo under {n}KB for an upload form? Choose your image below and the tool shrinks it to just under {n}KB while keeping it as sharp as the limit allows.",
      f"Portals that ask for {n}KB usually also want a JPG file. This tool outputs JPG. If the result looks too soft, upload a higher-resolution original, because tiny or already-compressed images have little left to give."))
uses = [
 ("signature-image-under-20kb","Compress Signature Image to 20KB",20,"Job and exam portals commonly ask for a scanned signature under 20KB. Crop the white space around your signature before compressing for the best result."),
 ("passport-photo-under-50kb","Reduce Passport Size Photo to 50KB",50,"Passport-size photos for application forms are often limited to around 50KB. Use a plain background and good lighting so the face stays clear after compression."),
 ("resume-photo-under-30kb","Resize Resume and Profile Photo to 30KB",30,"Many job sites limit profile photos to about 30KB. Start from a front-facing photo with even light."),
 ("photo-for-online-form-under-100kb","Reduce Photo for Online Form to 100KB",100,"Admission, exam and registration forms often cap photos at 100KB. Upload the original and let the tool find the best quality under the limit."),
 ("id-card-image-under-200kb","Compress ID Card Image to 200KB",200,"Scans of ID cards for verification usually need to be under 200KB while staying readable. Make sure all text is legible in the result before submitting."),
 ("document-scan-under-500kb","Compress Document Scan Image to 500KB",500,"Photographed or scanned documents can be large. This reduces them to 500KB while keeping text readable."),
]
for slug,t,n,tip in uses:
    pages.append((slug, t+" – Free Online Tool", t, f"{t} free. No upload to servers, works in your browser.", "image", n,
      f"{t.replace('Compress ','').replace('Reduce ','').replace('Resize ','')} – drop your image, get a file under {n}KB, and download it instantly.", tip))
for n in [100,200,300,500,1024,2048]:
    pages.append((f"compress-pdf-to-{n}kb" if n<1024 else f"compress-pdf-to-{n//1024}mb", f"Compress PDF to {lab(n)} – Free Online PDF Reducer",
      f"Compress PDF to {lab(n)}", f"Reduce PDF file size to under {lab(n)} for free. Runs in your browser, files are never uploaded.",
      "pdf", n,
      f"Need a PDF under {lab(n)} for an email or application portal? Choose your file and the tool shrinks it to fit.",
      "Best for scanned documents, forms and image-heavy PDFs. Pages are converted to compressed images, so text in the result cannot be selected or searched. Keep your original file as a backup."))


NOTES = {
 "compress-image-to-10kb":"10KB is extremely small. It suits tiny signatures, thumbnails and avatar fields. Photos lose fine detail at this size, so crop tightly to the subject first and avoid busy backgrounds.",
 "compress-image-to-15kb":"15KB limits show up on some older government and recruitment portals for signatures and thumb impressions. Dark ink on plain white paper compresses far better than a coloured background.",
 "compress-image-to-20kb":"20KB is one of the most searched sizes, mainly for signatures on job and exam forms. A signature in dark pen on white paper stays clear even at this size.",
 "compress-image-to-25kb":"25KB is common for small profile photos and signature fields. If the result looks blurry, crop closer to the face or signature first: fewer pixels means more quality for every KB.",
 "compress-image-to-30kb":"30KB fits many resume and application photos. Face photos on a plain background reach this size with little visible loss.",
 "compress-image-to-40kb":"40KB gives room for a clearer passport-style photo. Keep the background plain and the lighting even for the best look.",
 "compress-image-to-50kb":"50KB is a very common limit for passport-size photos on application portals. Faces hold up well when the original is sharp and evenly lit.",
 "compress-image-to-70kb":"70KB is a middle size used by some university and recruitment forms. Skin tones and printed text on badges usually stay readable.",
 "compress-image-to-100kb":"100KB is the standard limit on many registration forms. You keep good detail here, and most phone photos shrink to it with only mild softness.",
 "compress-image-to-150kb":"150KB suits document photos where small text must stay legible, such as the back of an ID or a stamped certificate corner.",
 "compress-image-to-200kb":"200KB is typical for ID card and certificate scans. Text in normal documents stays readable at this size.",
 "compress-image-to-300kb":"300KB fits larger document images, such as a full certificate page. Contrast between text and background matters more than raw resolution.",
 "compress-image-to-500kb":"500KB leaves room for full-page scans. Photograph documents flat and in good light, since shadows waste bytes.",
 "signature-image-under-20kb":"Sign with a dark pen on plain white paper, photograph or scan it in even light, crop tightly around the signature, then compress. Also check whether the portal sets a width and height in pixels.",
 "passport-photo-under-50kb":"Check whether the portal wants exact pixel dimensions, a white background and a centred head. Resize to those dimensions first, then compress last so the image is not degraded twice.",
 "resume-photo-under-30kb":"Choose a neat, front-facing photo, crop to head and shoulders, and avoid filters. Heavy editing adds noise that makes small files look worse.",
 "photo-for-online-form-under-100kb":"Check which file types the form accepts. This tool outputs JPG, which nearly every portal accepts. If your form needs PNG, convert after compressing.",
 "id-card-image-under-200kb":"Make sure all four corners of the card are visible and nothing is cut off. Because the image is processed in your browser, it is not sent to our servers, which matters for ID documents.",
 "document-scan-under-500kb":"Photograph the page flat in daylight, crop the edges, then compress. Dark text on a white page produces the smallest files.",
 "compress-pdf-to-100kb":"100KB is tiny for a PDF. One or two simple pages will fit; longer scans may need a higher target.",
 "compress-pdf-to-200kb":"200KB works for a single scanned page or a short form. Black-and-white scans compress best.",
 "compress-pdf-to-300kb":"300KB is common for one or two page attachments on application portals.",
 "compress-pdf-to-500kb":"500KB suits a short multi-page document such as a CV with a cover letter.",
 "compress-pdf-to-1mb":"1MB is a frequent limit for email attachments and upload forms. A few scanned pages usually fit comfortably.",
 "compress-pdf-to-2mb":"2MB leaves room for a handful of pages while keeping scans easy to read.",
}
def extras(slug, mode, n):
    note = NOTES.get(slug, "")
    mb = n/1024
    phone = 3072
    facts = (f"<h2>About {lab(n)}</h2><p>{note}</p>" if note else "")
    if mode == "image":
        facts += f"<p>For scale, {n}KB is about {mb:.2f}MB. A typical 3MB phone photo has to shrink roughly {phone/n:.0f} times to fit, so expect lower resolution and some softness. Cropping first keeps more detail.</p>"
        steps = ["Select your image (JPG, PNG or WebP).", f"Keep {lab(n)} selected as the target, or type your own size.", "Press Compress, check the preview, then download the result."]
    else:
        facts += f"<p>The tool rebuilds each page as a compressed image until the whole file fits under {lab(n)}. Documents with many pages need a higher target than short ones.</p>"
        steps = ["Select your PDF (up to 40 pages).", f"Keep {lab(n)} selected as the target, or type your own size.", "Press Compress and wait while pages are processed, then download."]
    howto = "<h2>How to use</h2><ol>" + "".join(f"<li>{x}</li>" for x in steps) + "</ol>"
    return howto + facts


GUIDES = [
("how-to-reduce-photo-size-for-online-form","How to Reduce Photo Size for an Online Form (Step by Step)","Learn how to get a photo under the KB limit on any online form without ruining the quality.",
"""<p>Online forms often reject photos with a message like "file must be under 50KB". Phone photos are usually several megabytes, so they need to shrink a lot. Here is a simple method that works for most forms.</p>
<h2>1. Read the exact requirement</h2><p>Check three things on the form: the maximum size (for example 50KB or 100KB), the allowed file type (usually JPG), and any required dimensions in pixels. Some forms also set a minimum size, so a file that is too small can be rejected too.</p>
<h2>2. Crop before you compress</h2><p>Crop away empty space around your face or document. Fewer pixels means the compressor can keep more detail inside the same file size.</p>
<h2>3. Compress to the target</h2><p>Open the <a href="/compress-image-to-50kb.html">image compressor</a>, choose your size, and download the result. Use a custom size if your form has an unusual limit.</p>
<h2>4. Check the result</h2><p>Zoom in and make sure your face or text is still clear. If it looks too soft, start again from the original photo, not from an already compressed copy. Compressing a compressed file twice lowers quality further.</p>
<h2>Common mistakes</h2><ul><li>Renaming a PNG to .jpg does not change its format.</li><li>Screenshots of photos are usually lower quality than the original.</li><li>Uploading a tiny image and expecting it to look sharp when the portal enlarges it.</li></ul>"""),
("how-to-compress-signature-for-job-application","How to Compress a Signature Image to 20KB for Job Applications","A practical guide to scanning, cropping and compressing a signature so it fits the size limit.",
"""<p>Many job and exam portals ask for a scanned signature under a small limit, often 20KB. A signature is mostly white space with a few dark lines, so it compresses well if you prepare it properly.</p>
<h2>Prepare the signature</h2><p>Sign with a dark pen, preferably black or dark blue, on plain white paper with no lines. Photograph it in daylight from directly above so there are no shadows. Shadows add grey tones that make the file larger.</p>
<h2>Crop tightly</h2><p>Crop so the signature fills most of the frame. If the form states a ratio such as 140 by 60 pixels, match that shape when cropping.</p>
<h2>Compress</h2><p>Use the <a href="/signature-image-under-20kb.html">signature compressor</a> and keep the 20KB target. If the signature still looks rough, try photographing it larger or on whiter paper rather than lowering the target.</p>
<h2>Final checks</h2><ul><li>The file type matches what the portal asks for.</li><li>Strokes are continuous, not broken into dots.</li><li>The file is under the limit but not far below any stated minimum.</li></ul>"""),
("passport-photo-size-requirements-for-online-forms","Passport Size Photo for Online Forms: What to Check Before Uploading","What portals usually require for passport-style photos and how to meet size limits without rejection.",
"""<p>Requirements differ for every website and country, so always follow the instructions on your own form. These are the points that usually matter.</p>
<h2>Background and lighting</h2><p>Most portals prefer a plain, light background and even lighting on the face. Avoid shadows, strong filters and glare from glasses.</p>
<h2>Framing</h2><p>Keep your face centred and facing the camera, with head and shoulders visible. Crop to the shape the form asks for before you compress.</p>
<h2>Dimensions versus file size</h2><p>Forms often set both pixel dimensions and a file size limit. Resize to the required dimensions first, then compress to the size limit as the last step. See the <a href="/passport-photo-under-50kb.html">passport photo compressor</a>.</p>
<h2>If the upload is rejected</h2><ul><li>Check the file type (JPG is the safest choice).</li><li>Check you did not go below a stated minimum size.</li><li>Try a different browser if the upload button does nothing.</li></ul>"""),
("jpg-vs-png-which-file-is-smaller","JPG vs PNG: Which File Format Is Smaller?","Understand the difference between JPG and PNG and which one to use when you have a size limit.",
"""<p>JPG and PNG are the two most common image formats, and they behave very differently when you need a small file.</p>
<h2>JPG</h2><p>JPG uses lossy compression. It throws away detail the eye is less likely to notice, which makes photos much smaller. You can choose how much quality to give up, which is exactly how a tool reaches a target like 50KB.</p>
<h2>PNG</h2><p>PNG is lossless, so it keeps every pixel. That is great for logos and screenshots with flat colours and sharp edges, but photos in PNG are often many times larger than the same photo in JPG.</p>
<h2>Which should you use for a form?</h2><p>For photos, signatures and scanned documents with a size limit, JPG is almost always the right choice. The <a href="/compress-image-to-100kb.html">image compressor</a> outputs JPG for that reason.</p>
<h2>When PNG is better</h2><p>Use PNG for logos, icons and images needing transparency, where sharp edges matter more than size.</p>"""),
("how-to-compress-pdf-for-email","How to Compress a PDF to Send by Email","Make a PDF small enough for email or an upload form, and learn what you give up when you do.",
"""<p>Email services and application portals often limit attachments. Scanned PDFs are the usual problem because each page is a large image.</p>
<h2>Why scanned PDFs are large</h2><p>A scan stores each page as a picture. A ten-page scan at high resolution can easily be many megabytes.</p>
<h2>How compression works</h2><p>The <a href="/compress-pdf-to-1mb.html">PDF compressor</a> turns each page into a compressed image and rebuilds the file until it fits your target. This works well for scans and forms.</p>
<h2>What you give up</h2><p>Because pages become images, you cannot select or search the text in the result. If you need searchable text, keep your original and use the compressed copy only for the upload.</p>
<h2>Tips</h2><ul><li>Split very long documents into parts if one file is too big.</li><li>Black and white scans are much smaller than colour scans.</li><li>Always keep your original file.</li></ul>"""),
("why-is-my-photo-blurry-after-compressing","Why Is My Photo Blurry After Compressing? How to Fix It","Common reasons photos lose quality when reduced to a small size and what you can do about it.",
"""<p>When a file must fit a strict size, something has to give. Understanding what helps you get the best result.</p>
<h2>The size limit is very small</h2><p>Going from a multi-megabyte photo to 20KB means discarding most of the data. Small targets always cost some sharpness.</p>
<h2>The source image is poor</h2><p>Dark, noisy or already compressed photos have less usable detail. Start from the best original you have.</p>
<h2>You compressed twice</h2><p>Every round of JPG compression loses detail. Always compress from the original, not a previous copy.</p>
<h2>How to get a better result</h2><ul><li>Crop tightly first so no bytes are spent on empty space.</li><li>Use good, even light and a plain background.</li><li>If the form allows it, pick the higher of the allowed sizes, such as <a href="/compress-image-to-100kb.html">100KB</a> instead of 50KB.</li></ul>"""),
("how-to-scan-a-document-with-your-phone-small-file","How to Scan a Document With Your Phone and Keep the File Small","Take clean document photos that compress to small sizes and stay readable.",
"""<p>A good scan is easier to compress than a messy photo. A few habits make a big difference.</p>
<h2>Lighting and angle</h2><p>Place the page flat on a table near a window. Hold the phone directly above it so the page looks like a rectangle, not a trapezoid.</p>
<h2>Avoid shadows</h2><p>Your hand and phone cast shadows that add grey areas. Shadows make files larger and text harder to read.</p>
<h2>Crop and straighten</h2><p>Crop to the edges of the page. Most phone gallery apps have a crop and straighten tool.</p>
<h2>Then compress</h2><p>Use the <a href="/document-scan-under-500kb.html">document compressor</a> for images, or the <a href="/compress-pdf-to-500kb.html">PDF compressor</a> if you have a PDF. Check that all text is still readable before uploading.</p>"""),
("what-is-a-kb-and-mb-file-size-explained","KB vs MB: File Sizes Explained Simply","A plain explanation of kilobytes and megabytes so file size limits make sense.",
"""<p>File size limits on forms are written in KB or MB. Here is what those mean in practice.</p>
<h2>The basics</h2><p>A kilobyte (KB) is a small unit. A megabyte (MB) is about 1,024 KB. So 1MB is roughly the same as 1,024KB, and a 2MB limit is about 2,048KB.</p>
<h2>What sizes look like</h2><ul><li>Under 50KB: a small, tightly cropped photo or a signature.</li><li>100KB to 500KB: a clearer photo or a scanned page.</li><li>Several MB: a typical photo straight from a modern phone.</li></ul>
<h2>Why it matters</h2><p>Websites set limits to save storage and speed up uploads. If your file is over the limit, you can shrink it with the <a href="/">image and PDF compressor</a>.</p>"""),
]
def guide_grp():
    li = "".join(f'<li><a href="/guides/{g[0]}.html">{g[1]}</a></li>' for g in GUIDES)
    return f"<h2>Guides</h2><ul class='links'>{li}</ul>"

def adblock():
    if not (ADSENSE_CLIENT and AD_SLOT): return ""
    return f'<div class="ad"><ins class="adsbygoogle" style="display:block" data-ad-client="{ADSENSE_CLIENT}" data-ad-slot="{AD_SLOT}" data-ad-format="auto" data-full-width-responsive="true"></ins><script>(adsbygoogle=window.adsbygoogle||[]).push({{}});</script></div>'
adhead = f'<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client={ADSENSE_CLIENT}" crossorigin="anonymous"></script>' if ADSENSE_CLIENT else ""

def linklist(cur):
    def grp(title, items):
        li = "".join(f'<li><a href="/{s}.html">{t}</a></li>' for s,t in items if s != cur)
        return f"<h2>{title}</h2><ul class='links'>{li}</ul>"
    im = [(p[0], p[2].replace("Compress Image to ","")) for p in pages if p[4]=="image" and p[0].startswith("compress-image-to-")]
    us = [(p[0], p[2]) for p in pages if p[4]=="image" and not p[0].startswith("compress-image-to-")]
    pd = [(p[0], p[2].replace("Compress PDF to ","PDF ")) for p in pages if p[4]=="pdf"]
    return grp("Compress image to a size",im)+grp("For forms and applications",us)+grp("Compress PDF",pd)+guide_grp()

BADGES = '<ul class="badges"><li>Free</li><li>100% private</li><li>No sign-up</li></ul>'
CSS = open("assets/style.css").read()
JS = open("assets/tool.js").read()
def shell(title, desc, canon, body):
    html = _shell(title, desc, canon, body)
    prefix = "../" if canon.startswith("/guides/") else ""
    html = html.replace('href="/"', f'href="{prefix or "./"}index.html"')
    html = html.replace('href="/', f'href="{prefix}')
    return html

def _shell(title, desc, canon, body):
    return f'''<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}"><link rel="canonical" href="{DOMAIN}{canon}">
<style>{CSS}</style>{adhead}</head><body>
<div class="topbar">A project by <a href="https://companyflow.co.uk" target="_blank" rel="noopener">CompanyFlow</a></div><header><div class="wrap"><a class="logo" href="/"><span class="mark">KB</span>{SITE}</a><nav><a href="/">Image</a><a href="/compress-pdf-to-200kb.html">PDF</a><a href="/guides.html">Guides</a></nav></div></header>
<main class="wrap">{body}</main>
<section class="brand"><div class="wrap"><div class="brandcard"><div><strong>{SITE} is a project by CompanyFlow</strong><span>Visit our website to see more from CompanyFlow.</span></div><a class="btn" href="https://companyflow.co.uk" target="_blank" rel="noopener">Visit companyflow.co.uk →</a></div></div></section><footer><div class="wrap"><a href="/guides.html">Guides</a><a href="/about.html">About</a><a href="/privacy.html">Privacy Policy</a><a href="/contact.html">Contact</a><p>© {datetime.date.today().year} {SITE}. All processing happens in your browser.</p><p>A project by <a href="https://companyflow.co.uk" rel="noopener">companyflow.co.uk</a></p></div></footer>
<script>{JS}</script></body></html>'''

def faq(mode, n):
    q = [("Is it free?","Yes, completely free with no sign-up."),
         ("Are my files uploaded anywhere?","No. Compression happens inside your browser and your file never leaves your device."),
         ("Why is my result slightly under the target?","The tool finds the highest quality that still fits under the limit you chose.")]
    return "<h2>Frequently asked questions</h2><div class='faq'>"+"".join(f"<h3>{a}</h3><p>{b}</p>" for a,b in q)+"</div>"

for slug,title,h1,desc,mode,n,intro,tip in pages:
    body = f'<h1>{h1}</h1><p class="sub">{intro}</p>{BADGES}<div class="card"><div class="tool" data-mode="{mode}" data-target="{n}"></div></div>{adblock()}{extras(slug,mode,n)}<h2>Tips for best results</h2><p>{tip}</p>{faq(mode,n)}{adblock()}{linklist(slug)}'
    open(f"{slug}.html","w").write(shell(title,desc,f"/{slug}.html",body))

home = f'''<h1>Compress Image or PDF to an Exact Size</h1><p class="sub">Get your photo, signature or document under 20KB, 50KB, 100KB or any limit. Free, private, no sign-up.</p>
{BADGES}<div class="tools"><div class="card"><h2>Image compressor</h2><div class="tool" data-mode="image" data-target="50"></div></div>
<div class="card"><h2>PDF compressor</h2><div class="tool" data-mode="pdf" data-target="200"></div></div></div>{adblock()}{faq("image",50)}{linklist("")}'''
open("index.html","w").write(shell(f"{SITE} – Compress Image & PDF to Exact KB Online","Free tool to compress images and PDFs to 20KB, 50KB, 100KB or any size. Private, works in your browser.","/",home))

open("about.html","w").write(shell(f"About {SITE}","About this free tool","/about.html",f"<h1>About {SITE}</h1><p>{SITE} is a free tool that helps you meet file size limits on application forms, exam portals and email attachments. Everything runs locally in your browser, so your files stay private.</p>"))
open("contact.html","w").write(shell(f"Contact {SITE}","Contact us","/contact.html",f"<h1>Contact</h1><p>Questions or feedback? Email us at <b>companyflow0@gmail.com</b>.</p>"))
open("privacy.html","w").write(shell(f"Privacy Policy – {SITE}","Privacy policy","/privacy.html",f"<h1>Privacy Policy</h1><p>Files you select are processed entirely in your browser and are never uploaded to our servers. We do not store your images or documents.</p><p>We may use third-party services such as Google AdSense and analytics, which can use cookies to serve ads and measure traffic. Google's use of advertising cookies enables it and its partners to serve ads based on your visits to this and other sites. You can opt out of personalized advertising at Google Ads Settings.</p><p>Contact: companyflow0@gmail.com. Last updated {datetime.date.today():%B %d, %Y}.</p>"))


os.makedirs("guides", exist_ok=True)
for slug,title,desc,body in GUIDES:
    others = "".join(f'<li><a href="/guides/{g[0]}.html">{g[1]}</a></li>' for g in GUIDES if g[0]!=slug)
    html = f'<h1>{title}</h1><p class="sub">{desc}</p>{body}{adblock()}<div class="card"><b>Need to compress a file now?</b> <a href="/">Use the free SizeTrim image and PDF compressor</a>.</div><h2>More guides</h2><ul class="links">{others}</ul>'
    open(f"guides/{slug}.html","w").write(shell(f"{title} | {SITE}", desc, f"/guides/{slug}.html", html))
idx = "".join(f'<li><a href="/guides/{g[0]}.html">{g[1]}</a></li>' for g in GUIDES)
open("guides.html","w").write(shell(f"Guides – {SITE}","Practical guides for resizing photos, signatures and PDFs for online forms.","/guides.html",f'<h1>Guides</h1><p class="sub">Practical help for meeting file size limits on forms and portals.</p><ul class="links">{idx}</ul>'))

urls = ["/"]+[f"/{p[0]}.html" for p in pages]+["/guides.html"]+[f"/guides/{g[0]}.html" for g in GUIDES]+["/about.html","/privacy.html","/contact.html"]
open("sitemap.xml","w").write('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+"".join(f"<url><loc>{DOMAIN}{u}</loc></url>" for u in urls)+"</urlset>")
open("robots.txt","w").write(f"User-agent: *\nAllow: /\nSitemap: {DOMAIN}/sitemap.xml\n")
print(len(pages)+4+len(GUIDES)+1, "pages built")
