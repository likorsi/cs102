//нормализация[0,1] рейтинга
function Noramalize_rating(){
	var max_rating = 5000;
	
	for (var x = 0; x < players.length; x++)
		players[x][0] = players[x][0] / max_rating;
	return players;
}


function balance() {
	 Noramalize_rating();
   /*баланс по классу
		'dps':0.8, 'tank':0.6, 'support':0.4 */
		for (var x = 0; x < players.length; x++){
			if (players[x][1] === 'dps'){
				arr_result[x] = players[x][0] * 0.8;
			} else if (players[x][1] === 'tank'){
				arr_result[x] = players[x][0] * 0.6;
			} else if (players[x][1] === 'support'){
				arr_result[x] = players[x][0] * 0.4;
			}
      //баланс при игре пользователя за одиного персонажа/класс 
      if (players[x][2] === 1){
      arr_result[x] *= 0.6;
      } else if (players[x][3] === 1){
      arr_result[x] *= 0.9;
      }   
		}
    
	return arr_result;
 }

	

function sort_rating(){
    var n = arr_result.length;
    for (var i = 0; i < n-1; i++)
     { for (var j = 0; j < n-1-i; j++)
        { if (arr_result[j+1] < arr_result[j])
           { var t = arr_result[j+1]; arr_result[j+1] = arr_result[j]; arr_result[j] = t; }
        }
     }   
    a = arr_result.reverse();
    arr_result = a;

    return arr_result;
}

/* вложенный массив с критериями игроков из лобби
структура: [[SR, class, one_class_player, one_character_player]]
пример: players = [[1500, 'dps', 0, 0], [4756, 'support', 1, 0]] */
var players = [
[2000, 'dps', 0, 0], 
[4500, 'support', 1, 0],
[2500, 'dps', 0, 0], 
[3500, 'tank', 1, 1]
];

var arr_result = []; //итоговый рейтинг игрока

balance();
sort_rating();

var team1 = [];
var team2 = [];

for (var x = 0; x < arr_result.length; x++){
	team1.push(arr_result[x]);
	team2.push(arr_result[x+1]);
	x += 1;
}

console.log(true)
