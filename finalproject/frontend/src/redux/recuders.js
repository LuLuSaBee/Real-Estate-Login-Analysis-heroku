import { combineReducers } from "redux";
import {
  INIT_REALESTATEDATA,
  UPDATE_REALESTATEDATA,
  INIT_COLUMNDATA,
  INIT_DASHBOARDDATA,
  UPDATE_CALCULATORPARAM,
} from "./actions";

function realEstateData(state = [], action) {
  switch (action.type) {
    case INIT_REALESTATEDATA:
      return action.realEstates;
    case UPDATE_REALESTATEDATA:
      return [...state, ...action.realEstates];
    default:
      return state;
  }
}

function columnData(state = [], action) {
  switch (action.type) {
    case INIT_COLUMNDATA:
      return action.columnData;
    default:
      return state;
  }
}

function dashboardData(state = [], action) {
  switch (action.type) {
    case INIT_DASHBOARDDATA:
      return action.dashBoardData;
    default:
      return state;
  }
}

function calculatorParam(
  state = { loan: "", year: 20, timeOfYear: 12, interestRate: 1.88 },
  action
) {
  switch (action.type) {
    case UPDATE_CALCULATORPARAM:
      return { ...state, ...action.params };
    default:
      return state;
  }
}

export default combineReducers({
  realEstateData,
  columnData,
  dashboardData,
  calculatorParam,
});
