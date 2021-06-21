export const INIT_REALESTATEDATA = "INIT_REALESTATEDATA";
export const UPDATE_REALESTATEDATA = "UPDATE_REALESTATEDATA";
export const INIT_COLUMNDATA = "INIT_COLUMNDATA";
export const INIT_DASHBOARDDATA = "INIT_DASHBOARDDATA";
export const UPDATE_CALCULATORPARAM = "UPDATE_CALCULATORPARAM";

export const initRealEstateData = (realEstates) => ({
  type: INIT_REALESTATEDATA,
  realEstates,
});

export const updateRealEstateData = (realEstates) => ({
  type: UPDATE_REALESTATEDATA,
  realEstates,
});

export const initColumnData = (columnData) => ({
  type: INIT_COLUMNDATA,
  columnData,
});

export const initDashBoardData = (dashBoardData) => ({
  type: INIT_DASHBOARDDATA,
  dashBoardData,
});

export const updateCalculatorParam = (params) => ({
  type: UPDATE_CALCULATORPARAM,
  params,
});
