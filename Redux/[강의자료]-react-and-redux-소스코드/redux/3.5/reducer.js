import * as ActionsType from './action-type.js';

// export function reducer(state = { count: 0 }, action) {
  //   switch(action.type) {
    //     case ActionsType.INCREASE:
    //       return { ...state, count: state.count + 1 };
    //     case ActionsType.DECREASE:
    //       return { ...state, count: state.count - 1 };
    //     case ActionsType.RESET:
    //       return { ...state, count: 0 };
    //     default: 
    //       return { ...state };
    //   }
    // }

const InitializeState = { count:0 };
export function reducer(state = InitializeState, action) {
  switch(action.type) {
    case ActionsType.INCREASE:
      return { ...state, count: state.count + 1 };
    case ActionsType.DECREASE:
      return { ...state, count: state.count - 1 };
    case ActionsType.RESET:
      return { ...state, count: 0 };
    default: 
      return { ...state };
  }
}