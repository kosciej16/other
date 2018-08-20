seconds = 4
lags = 38

results = {}


def f(seconds, lags):
	if (seconds,lags) in results:
		return results[(seconds, lags)]
	# Pierwszy parametr rekursji to przewaga jednej drużyny (moze być ujemna).
	# Kończymy, gdy nie ma więcej lagów. Jeśli liczba sekund jest większa od 0, to nie liczymy czynnika.
	result = (seconds <= 0 if lags == 0 else (
		# Wzór rekurencyjny: W każdym lagu serwera istnieje 9 możliwości:
		# Trzy przypadki, gdy obie drużyny doświadczyły tego samego laga (obie zero/jedną/dwie sekundy).
		3*f(seconds, lags-1) +
		# Po dwa przypadki, w których jedna z nich doświadczyła laga o sekundę dłuższego od drugiej.
		2*f(seconds+1, lags-1) + 2*f(seconds-1, lags-1) +
		# I po jednym, gdzie różnica była dwusekundowa.
		f(seconds-2, lags-1) + f(seconds+2, lags-1)
	))
	results[(seconds, lags)] = result
	return result


# Czterosekundowy lag, wzór analogiczny
def f4(seconds, lags):
	if (seconds,lags) in results:
		return results[(seconds, lags)]
	result = (seconds <= 0 if lags == 0 else (
		5*f4(seconds, lags-1) +
		4*f4(seconds-1, lags-1) + 4*f4(seconds+1, lags-1) +
		3*f4(seconds-2, lags-1) + 3*f4(seconds+2, lags-1) +
		2*f4(seconds-3, lags-1) + 2*f4(seconds+3, lags-1) +
		f4(seconds-4, lags-1) + f4(seconds+4, lags-1)
	))
	results[(seconds, lags)] = result
	return result


# Dzielimy, przez liczbę wszystkich możliwości
print(f(seconds,lags)/9**lags) # 0.3117160404565305
results.clear()
print(f4(seconds,lags)/25**lags) # 0.3884453173801041

results.clear()
# Przy nieco większych różnicach, losowość dramatycznie spada.
a_lot_seconds = 20
print(f(a_lot_seconds,lags)/9**lags) # 0.0029595206139032527
