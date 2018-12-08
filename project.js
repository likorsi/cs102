// Имеющиеся классы (для удобства)
const HERO_CLASS = {
	DPS: 'dps',
	TANK: 'tank',
	SUPPORT: 'support'
}

// Коэффициенты влияния класса на баланс
const HERO_CLASS_RATIO = {
	[HERO_CLASS.DPS]: 0.8,
	[HERO_CLASS.TANK]: 0.6,
	[HERO_CLASS.SUPPORT]: 0.4
}

// Получение нормализованного рейтинга для игрока
function getNormalizedRating(sr) {
	const maxRating = 5000

	return sr / maxRating
}

// Проверка на то, что игрок играет персами одного класса
function isOneClass(classesArray) {
	return classesArray.length === 1
}

// Получаем модифицированный массив игроков с новым полем balanceRatio,
// которое высчитывается для игрока в этой функции (переписанная функция balance).
function getPlayersWithBalanceRatio(players) {
	return players.map(function(player) {
		const normalizedSR = getNormalizedRating(player.sr)
		const mainClass = player.classes[0]

		let balanceRatio = normalizedSR * HERO_CLASS_RATIO[mainClass]

		if (isOneClass(player.classes)) {
			balanceRatio *= 0.6
		} else if (player.isOneTrick) {
			balanceRatio *= 0.9
		}

		// Копируем все поля игрока в новую переменную, чтобы не изменить инстанс игрока
		// (почему так надо - объясню)
		let newPlayer = Object.assign(player)

		newPlayer.balanceRatio = balanceRatio

		return newPlayer
	})
}

const players = [
	{
		id: '1',
		sr: 2000,
		classes: [HERO_CLASS.DPS, HERO_CLASS.SUPPORT],
		isOneTrick: false
	},
	{
		id: '2',
		sr: 4500,
		classes: [HERO_CLASS.SUPPORT],
		isOneTrick: false
	},
	{
		id: '3',
		sr: 2500,
		classes: [HERO_CLASS.DPS, HERO_CLASS.TANK],
		isOneTrick: false
	},
	{
		id: '4',
		sr: 3500,
		classes: [HERO_CLASS.TANK],
		isOneTrick: true
	},
]

const playersWithBalanceRatio = getPlayersWithBalanceRatio(players)

console.log(players, playersWithBalanceRatio)
