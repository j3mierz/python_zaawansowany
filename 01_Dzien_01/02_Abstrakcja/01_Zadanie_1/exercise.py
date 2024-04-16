import random

random_usdpln_rates = [3.5]
for _ in range(50):
    random_usdpln_rates.append(round(random_usdpln_rates[-1] + random.random() * 0.2 - 0.1, 2))


class CommandPrompt:

    def __init__(self, buy, sell, wait):
        self.buy = buy
        self.sell = sell
        self.wait = wait

    def ask(self):
        result = input('Decision [b/s/w/buy/sell/wait]: ')
        while result not in self.buy + self.sell + self.wait:
            print(f'Invalid choice: {result}')
            result = input('Decision [b/s/w/buy/sell/wait]: ')
        return result


class Wallet:
    def __init__(self, pln, usd):
        self.pln = float(pln)
        self.usd = float(usd)

    def convert_pln_to_usd(self, usdpln_rate):
        return round(self.pln / usdpln_rate, 2)

    def convert_usd_to_pln(self, usdpln_rate):
        return round(usdpln_rate * self.usd, 2)


choice = CommandPrompt(['buy', 'k'], ['sell', 's'], ['wait', 'w', ''])


def main(usdpln_rates):
    currency = Wallet(100, 0)
    for usdpln_rate in usdpln_rates:
        print(f'Balance: {round(currency.pln, 2)} PLN, ${round(currency.usd, 2)}, rate {usdpln_rate}')
        comm = choice.ask()
        if comm in ('k', 'buy'):
            currency.usd += currency.convert_pln_to_usd(usdpln_rate)
            currency.pln = 0
        elif comm in ('s', 'sell'):
            currency.pln += currency.convert_usd_to_pln(usdpln_rate)
            currency.usd = 0

    currency.pln += currency.convert_usd_to_pln(usdpln_rate)
    currency.usd = 0
    print(f'Your result: {currency.pln} PLN!')


if __name__ == '__main__':
    main(random_usdpln_rates)
