import azure.functions as func
import logging
import telegram
import os


app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="f_httpt_rigger_test")
def f_httpt_rigger_test(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    challenge = req.params.get("challenge")

    if challenge:
        return func.HttpResponse(challenge, status_code=200)
    
    t = telegram.Telegram(bot_token=os.environ.get("TELEGRAM_BOT_TOKEN"),
                          chat_id=os.environ.get("TELEGRAM_CHAT_ID"))
    t.send_telegram_message("This is a test message!")
    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )