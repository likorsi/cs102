//нормализация[0,1] рейтинга
function normalize_rating(players) {
	var max_rating = 5000;
	var arr_rating = []  //нормализованный массив

	for (var x = 0; x < players.length; x++)
		arr_rating[x] = players[x] / max_rating;
	return arr_rating;
}


function balance(arr, class) {
	Normalize_rating();

	var arr_result = []; //итоговый рейтинг игрока

	for (var x = 0; x < arr_rating.length; x++){
		arr_result[x] = arr_rating[x] * class;

		if (one_class_player = True)
			arr_result[x] *= 0.6
		if (one_character_player = True)
			arr_result[x] *= 0.9
	}
	
	return arr_result;
}


var players = []; //вложенный массив с рангами игроков для сортировки
/* структура: [[SR, class, one_class_player, one_character_player]]
пример: players = [[1500, 'dps', True, False], [4756, 'support', False. False]] */
var class: {'dps':0.8, 'tank':0.6, 'support':0.4}

balance(players, class);


var team1 = [];
var team2 = [];

for (var x = 0; x < arr_result.length; x++){
	team1.push(arr_result[x]);
	team2.push(arr_result[x+1]);
	x += 1;
}
