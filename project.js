//нормализация[0,1] рейтинга
function Normalize_rating(players) {
	var max_rating = 5000;
	var arr_rating = []  //нормализованный массив

	for (var x = 0; x < players.length; x++)
		arr_rating[x] = players[x][0] / max_rating;
	return arr_rating;
}


function Balance(players, class) {
	normalize_rating();

	var arr_result = []; //итоговый рейтинг игрока

	for (var x = 0; x < arr_rating.length; x++){
		var class: {'dps':0.8, 'tank':0.6, 'support':0.4};

		arr_result[x] = arr_rating[x] * class.players[x][1];
	
		if (players[x][2] == True)
			arr_result[x] *= 0.6;
		if (players[x][3] == True)
			arr_result[x] *= 0.9;
	}
	
	return arr_result;
}


function Sort_rating(arr_result){
    var n = arr_result.length;
    for (var i = 0; i < n-1; i++)
     { for (var j = 0; j < n-1-i; j++)
        { if (arr_result[j+1] < arr_result[j])
           { var t = arr_result[j+1]; arr_result[j+1] = arr_result[j]; arr_result[j] = t; }
        }
     }                     
    return arr_result;
}


/* вложенный массив с критериями игроков из лобби
структура: [[SR, class, one_class_player, one_character_player]]
пример: players = [[1500, 'dps', True, False], [4756, 'support', False. False]] */
var players = [];

balance();
sort_rating();

var team1 = [];
var team2 = [];

for (var x = 0; x < arr_result.length; x++){
	team1.push(arr_result[x]);
	team2.push(arr_result[x+1]);
	x += 1;
}
