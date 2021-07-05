# NEAR To BRL price on Twitter

:brazil: :brazil: :brazil:

Tweeta o preço de NEAR convertido para BRL duas vezes por dia. Você pode conferir um exemplo [aqui](https://twitter.com/NearBrl).

## Setup

Esse projeto foi feito usando `Python 3.9.6`

1. Instale as dependencias: `pip install -r requirements.txt`
2. Crie um arquivo .env: `mv .env.example .env`
3. Popule o arquivo .env com as credenciais (tutorial abaixo)
4. Rode `python main.rb`

## Pegar Credenciais

#### CoinMarketCap
1. Acesse [CoinMarketCap](https://pro.coinmarketcap.com/signup) e crie uma conta de desenvolvedor
2. Vefique sua nova conta
3. Pegue a Api Key e adicione no .env (`CMC_API_KEY`)

#### Twitter
1. Acesse [Twitter Developer](https://developer.twitter.com/en/apply-for-access) e aplique para uma conta de desenvolvedor
2. Espere... Eles demoram algumas horas para aprovar seu pedido
3. Crie um projeto
4. Crie um app
5. Regenere e pege as Consumer Keys (`TWITTER_API_KEY` and `TWITTER_SECRET_API_KEY`)
6. Regenere e pege as Authentication Tokens (`TWITTER_ACCESS_TOKEN` and `TWITTER_SECRET_ACCESS_TOKEN`)

---

:us: :us: :us:

Tweets the NEAR price converted to BRL twice a day. You can check an example [here](https://twitter.com/NearBrl).

## Setup

This project was made using `Python 3.9.6`

1. Install dependencies: `pip install -r requirements.txt`
2. Create .env file: `mv .env.example .env`
3. Populate the .env file with credentials (tutorial below)
4. Run `python main.rb`

## Get Credentials

#### CoinMarketCap
1. Go to [CoinMarketCap](https://pro.coinmarketcap.com/signup) and create an developer account
2. Verify your new account
3. Get the Api Key and add to .env (`CMC_API_KEY`)

#### Twitter
1. Go to [Twitter Developer](https://developer.twitter.com/en/apply-for-access) and apply for a developer account
2. Wait... They took some hours to accept the request
3. Create a project
4. Create an app
5. Regenerate and get the Consumer Keys (`TWITTER_API_KEY` and `TWITTER_SECRET_API_KEY`)
6. Regenerate and get the Authentication Tokens (`TWITTER_ACCESS_TOKEN` and `TWITTER_SECRET_ACCESS_TOKEN`)
