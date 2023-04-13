import { createStore, actionCreator } from './redux.js'; //actionCreator : actions에서 사용함
import { reducer } from './reducer.js'
// import { INCREASE } from './action-type.js'  > actions에서 사용함
import { increase } from './actions.js'

const store = createStore(reducer);

store.subscribe(function() {
  console.log(store.getState());
});

// store.dispatch({ type: INCREASE });
// store.dispatch(actionCreator(INCREASE)); //위 문구가 개선됨
// store.dispatch(actionCreator(INCREASE, 1)); //payload가 있는 경우 파라미터에 포함
store.dispatch(increase()); //actions.js를 통해 위 문구가 개선됨
