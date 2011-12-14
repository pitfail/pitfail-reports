
Shares (model package)
- Attributes
    - +shares: BigDecimal
    - +<<operator>> -: Dollars
    - +<<operator>> ###: String
- Methods
    - +<<constructor>>(BigDecimal)
    - +<<constructor>>(String>
    - /compare(Shares): Int
    - +<<operator>> +(Shares): Shares
    - +<<operator>> -(Shares): Shares
    - +<<operator>> *(Price): Dollars
    - +<<operator>> *(Scale): Shares

Price (model package)
- Attributes
    - +price: BigDecimal
    - +<<operator>> $: String
- Methods
    - +<<constructor>>(BigDecimal)
    - +<<constructor>>(String)
    - /compare(Price): Int
    - +<<operator>> +(Price): Price
    - +<<operator>> -(Price): Price
    - +<<operator>> *(Shares): Dollars
    - +<<operator>> *(Scale): Price

Dollars (model package)
- Attributes
    - +dollars: BigDecimal
    - +<<operator>> -: Dollars
    - +<<operator>> $: String
- Methods
    - +<<constructor>>(BigDecimal)
    - +<<constructor>>(String)
    - +/compare(Dollars): Int
    - +<<operator>> +(Dollars): Dollars
    - +<<operator>> -(Dollars): Dollars
    - +<<operator>> *(Scale): Dollars
    - +<<operator>> -/-(Price): Shares
    - +<<operator>> /-/(Price): Shares

Scale (model package)
- Attributes
    - +price: BigDecimal
    - +<<operator>> -: Scale
    - +<<operator>> %: String
- Methods
    - +<<constructor>>(BigDecimal)
    - +<<constructor>>(String)
    - /compare(Scale): Int
    - +<<operator>> +(Scale): Scale
    - +<<operator>> -(Scale): Scale
    - +<<operator>> *(Price): Price
    - +<<operator>> *(Shares): Shares
    - +<<operator>> *(Scale): Scale

Stock (model.schema package)
- Attributes
    - +symbol: String
    - +toString: String

Quote (model.schema package)
- Attributes
    - +stock: Stock
    - +exchange: String
    - +price: Price
    - +updateTime: ateTime
    - +info: QuoteInfo
    - +toString: String
- Methods
    - /equals(Quote): Boolean

QuoteInfo (model.schema package)
- Attributes
    - +percentChange: Option[BigDecimal]
    - +openPrice: Option[BigDecimal]
    - +lowPrice: Option[BigDecimal]
    - +highPrice: Option[BigDecimal]
    - +dividendShare: Option[BigDecimal]
- Methods
    - /equals(Quote): Boolean

StockDatabase (stockdata package)
- Methods
    - +getQuote(Stock): Quote
    - +getQuotes(Seq[Stock]): Seq[Quote]

YahooYQLStockDatabase (stockdata package)
- Attributes
    - -queryService: HttpQueryService
- Methods
    - +<<constructor>>(HttpQueryService)
    - +getQuote(Stock): Quote
    - +getQuotes(Seq[Stock]): Seq[Quote]

YahooCSVStockDatabase (stockdata package)
- Attributes
    - -queryService: HttpQueryService
- Methods
    - +<<constructor>>(HttpQueryService)
    - +getQuote(Stock): Quote
    - +getQuotes(Seq[Stock]): Seq[Quote]

CachingStockDatabase (stockdata package)
- Attributes
    - -database: StockDatabase
    - -cache: Map[Stock, Quote]
- Methods
    - +<<constructor>>(StockDatabase)
    - +getQuote(Stock): Quote
    - +getQuotes(Seq[Stock]): Seq[Quote]

FailoverStockDatabase (stockdata package)
- Attributes
    - databases: Seq[StockDatabase]
- Methods
    - +<<constructor>>(Seq[StockDatabase])
    - +getQuote(Stock): Quote
    - +getQuotes(Seq[Stock]): Seq[Quote]

HomeScreen (android package)
 - Attributes
    - -activity: Activity
    - -spinner: Spinner
    - -indexOfUserNameForSpinner: Int
    - -search: Button
    - -sell: Button
    - -team: Button
    - -leaderboard: Button
    - -cashText: TextView
    - -ticker: AutoCompleteTextView
    - -companies: String[*] {unique}
 - Methods
    - +onCreate(Bundle): Unit
    - +onClick(View): Unit
    - +afterTextChanged(Editable): Unit
    - +beforeTextChanged(CharSequence, Int, Int, Int): Unit
    - +onTextChanged(CharSequence, Int, Int, Int): Unit

BuyDetail (android package)
 - Attributes
    - -tickerName: TextView
    - -buy: Button
    - -activity: Activity
    - -tickerString: String
    - -valueString: ArrayList<String>
 - Methods
    - +onCreate(Bundle): Unit
    - +ImageOperations(String, String): Drawable
    - +fetch(String): Object

PortfolioDetail (android package)
 - Attributes
    - -cashText: TextView
    - -portfolioHeader: TextView
    - -selectedPortfolio: String
 - Methods
    - onCreate(Bundle): Unit

NewTeam (android package)
 - Attributes
    - -portfolio: EditText
    - -invite: EditText
    - -inviteButton: Button
    - -activity: Activity
 - Methods
    - +onCreate(Bundle): Unit
    - +onClick(View): Unit

LeaderBoard (android package)
 - Methods
    - onCreate(Bundle): Unit

PollingService (android package)
 - Attributes
    - TAG: String { readonly }
    - timer: Timer
    - update_id: Int
 - Methods
    - onBind(Intent): IBinder
    - onCreate(): Unit
    - onDestroy(): Unit
