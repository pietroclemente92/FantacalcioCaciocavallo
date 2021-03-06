import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext
import os
PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1734872566:AAFuWSq0o5tF9ebLlH5C1XtZ0XgzLOyUCyQ'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Benevenuto partecipante. Io sono CacioBot, il tuo assistente personale. Se è la prima volta che mi utilizzi, clicca o scrivi /commands_fantacacio per visionare la tabella dei comandi fantacaio, altrimenti utilizza /commands_sites per visionare la tabella dei comandi siti.')
    
def commands_fantacacio(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Timeout Formazione", callback_data='/timeout_formazione'),
            InlineKeyboardButton("Voto d'Ufficio", callback_data='/voto_ufficio'),
        ],
        [
            InlineKeyboardButton("Quotazione", callback_data='/quotazione'),
            InlineKeyboardButton("Moduli", callback_data='/moduli'),
        ],
        [
            InlineKeyboardButton("Regola Rinvio", callback_data='/regola_rinvio'),
            InlineKeyboardButton("Regola Infortuni Gravi", callback_data='/regola_infortuni_gravi'),
        ],
        [
            InlineKeyboardButton("Bonus & Malus", callback_data='/bonus_malus'),
            InlineKeyboardButton("Gestione Competizioni", callback_data='/gestione_competizioni'),
        ],
        [
            InlineKeyboardButton("Regolamento Cacio", callback_data='/regolamento')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Comandi disponibili', reply_markup=reply_markup)
    
def commands_sites(update: Update, context: CallbackContext) -> None:
    """Sends a message with three inline buttons attached."""
    keyboard = [
        [
            InlineKeyboardButton("Diretta", callback_data='/diretta'),
            InlineKeyboardButton("Probabili Formazioni", callback_data='/fanta_probabili_formazioni'),
        ],
        [
            InlineKeyboardButton("Regolamento Leghe Private", callback_data='/fanta_regolamento_leghe_private')
        ],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('Comandi disponibili', reply_markup=reply_markup)
    
def button(update: Update, context: CallbackContext) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    # CallbackQueries need to be answered, even if no notification to the user is needed
    # Some clients may have trouble otherwise. See https://core.telegram.org/bots/api#callbackquery
    query.answer()
    #cqd = update.callback_query.data
    #message_id = update.callback_query.message.message_id
    #update_id = update.update_id
    #if cqd == '/quotazione':
    query.edit_message_text(text=f"Cliccare sul comando: {query.data}")
        
def testing(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Use /start to test this bot.")
    
#fantacalcio commands - regulation
#---------------------------------------------------------------------------------------------------------------------------------------------
def quotazione(update, context):
    """Send a message when the command /quotazione is issued."""
    update.message.reply_text('Quando un giocatore verrà chiamato, sarà considerata come base d’asta la sua quotazione attuale (QA al momento dell’asta) della lista di Fantacalcio. È necessario rimanere sempre con i crediti sufficienti per completare la propria rosa. ')

def moduli(update, context):
    """Send a message when the command /moduli is issued."""
    update.message.reply_text('I moduli possibili sono: 5-3-2, 5-4-1, 4-3-3, 4-4-2, 3-4-3, 3-5-2.')  
    
def timeout_formazione(update, context):
    """Send a message when the command /timeout_formazione is issued."""
    update.message.reply_text('La formazione va schierata entro 30 minuti antecedenti il primo anticipo di giornata. In caso di eventuali problemi contattare uno degli amministratori di lega. Qualora la formazione non venisse consegnata, verrà inserita in automatico quella schierata nella giornata precedente.')

def regolamento(update, context):
    update.message.reply_text('https://github.com/pietroclemente92/FantacalcioCaciocavallo/raw/master/Regolamento_Fantacalcio.docx')
    
def voto_ufficio(update, context):
    update.message.reply_text('In caso di eventuali buchi nella formazione, ogni partecipante avrà diritto ad una e una sola riserva d’ufficio dal voto 4 [giocatore di movimento e portiere].')

def regola_rinvio(update, context):
    update.message.reply_text('In caso di rinvio di una partita oltre il successivo turno di campionato, sarà assegnato il 6 d’ufficio a tutti i giocatori delle due squadre in questione.')
    
def regola_infortuni_gravi(update, context):
    update.message.reply_text('In caso un giocatore subisca un infortunio che preveda la conclusione della stagione, morte, infarto ed eventuali altri stati gravi che prevedono l’allontanamento dai campi, verrà tagliato dalla formazione del partecipante e potrà essere sostituito con un giocatore di pari o inferiore QA di acquisto.')
    
def bonus_malus(update, context):
    update.message.reply_text('I bonus e i malus applicati sono i seguenti: goal segnato (+3), goal su rigore (+3), rigore sbagliato (-3), assist (+1), ammonizione (-0.5), espulsione (-1), autogoal (-3), portiere imbattuto (+1), goal subito da portiere (-1 per ognuno). Viene applicato il bonus/malus di rendimento in base al numeri di sufficienze di voti senza bonus e malus: otto (+1), nove (+2). Dieci (+3), undici (+5). I punteggi vengono invertiti in caso di tre sufficienze in giù.')
    
def gestione_competizioni(update, context):
    update.message.reply_text('La competizione prevede un campionato con classifica tabulare e una coppa con fase a gironi ed eliminazione diretta. La coppa prevede due gruppi di quattro partecipanti nel quale i primi due classificati di entrambi i gruppi passeranno alla fase ad eliminazione diretta. Durante la seguente fase i partecipanti si sfideranno in due partita (andata e ritorno). In caso di eventuali pareggi, si decreterà un vincitore tramite i punti fantacalcio accumulati durante le due sfide. Tuttavia, qualora non bastasse tale metodo, si decreterà un vincente tramite tempi supplementari e rigori. Il campionato prevede una sfida a modalità tutti contro tutti a giornate. In caso di eventuali pareggi nei punteggi accumulati, si provvederà a tener conto dei punti fantacalcio o eventuali differenze reti.')
    
#fantacalcio commands - sites
def fanta_regolamento_leghe_private(update, context):
    update.message.reply_text('https://www.fantacalcio.it/regolamenti/leghe-private')
    
def fanta_probabili_formazioni(update, context):
    update.message.reply_text('https://www.fantacalcio.it/probabili-formazioni-serie-a')
    
def diretta(update, context):
    update.message.reply_text('https://www.diretta.it/serie-a')
    
def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    
    #fantacalcio commands - regulation
    dp.add_handler(CommandHandler("quotazione", quotazione))
    dp.add_handler(CommandHandler("moduli", moduli))
    dp.add_handler(CommandHandler("timeout_formazione", timeout_formazione))
    dp.add_handler(CommandHandler("voto_ufficio", voto_ufficio))
    dp.add_handler(CommandHandler("regola_rinvio", regola_rinvio))
    dp.add_handler(CommandHandler("regola_infortuni_gravi", regola_infortuni_gravi))
    dp.add_handler(CommandHandler("bonus_malus", bonus_malus))
    dp.add_handler(CommandHandler("gestione_competizioni", gestione_competizioni))
    dp.add_handler(CommandHandler("regolamento", regolamento))
    
    #fantacalcio commands - sites
    dp.add_handler(CommandHandler("fanta_regolamento_leghe_private", fanta_regolamento_leghe_private))    
    dp.add_handler(CommandHandler("fanta_probabili_formazioni", fanta_probabili_formazioni))
    dp.add_handler(CommandHandler("diretta", diretta))
    
    #fantacalcio commands - tables
    dp.add_handler(CommandHandler("commands_fantacacio", commands_fantacacio))
    dp.add_handler(CommandHandler("commands_sites", commands_sites))
    dp.add_handler(CallbackQueryHandler(button))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://fantacalciocaciocavallo.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()
