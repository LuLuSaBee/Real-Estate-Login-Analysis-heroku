export const routePath = {
  homepage: "/",
  dataRetrieval: "/select",
  loanCalculator: "/calculator",
};

import HomePage from "./views/HomePage";
import DataRetrieval from "./views/DataRetrieval";
import LoanCalculator from "./views/LoanCalculator";
export const navData = [
  {
    path: routePath.homepage,
    name: "首頁",
    icon: "home",
    component: HomePage,
  },
  {
    path: routePath.dataRetrieval,
    name: "資料檢索",
    icon: "search",
    component: DataRetrieval,
  },
  {
    path: routePath.loanCalculator,
    name: "貸款計算機",
    icon: "apps",
    component: LoanCalculator,
  },
];
