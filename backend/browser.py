from pyppeteer import launch
import asyncio


# Create websocket server

#TODO: adding a way to find the path of google chrome, and make it run headless
async def main():
    browser = await launch(executablePath="/usr/bin/google-chrome-stable", headless=False,
                           args=["--ignore-certificate-errors", "--use-fake-ui-for-media-stream","--enable-logging --v=1"],
                           )
    page = await browser.newPage()
    await page.goto("https://127.0.0.1:4443/", waitUntil="networkidle0")

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
    # Start and run websocket server forever
    asyncio.get_event_loop().run_forever()
