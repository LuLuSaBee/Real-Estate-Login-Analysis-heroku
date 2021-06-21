import React from "react";
import { connect } from "react-redux";
import { updateCalculatorParam } from "../redux/actions";
import CustomerTable from "../components/customerTable";
import TextField from "@material-ui/core/TextField";

class LoanCalculator extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;
    this.state = {
      table: [],
    };
  }

  componentDidMount() {
    this.calculate({ ...this.props.calculatorParam });
  }

  handleChangeText = (e) => {
    const { name, value } = e.target;
    if (/[0-9]+(\.[0-9])*/.test(value)) {
      this.props.dispatch(updateCalculatorParam({ [name]: value }));
      this.calculate({ ...this.props.calculatorParam, [name]: value });
    } else {
      alert("只能輸入數字");
    }
  };

  calculate = (data) => {
    let { loan, year, timeOfYear, interestRate } = data;
    if (
      !(
        /[0-9]+(\.[0-9])*/.test(loan) &&
        /[0-9]+(\.[0-9])*/.test(year) &&
        /[0-9]+(\.[0-9])*/.test(timeOfYear) &&
        /[0-9]+(\.[0-9])*/.test(interestRate)
      )
    ) {
      return;
    }

    loan = parseInt(loan) * 10000;
    year = parseInt(year);
    timeOfYear = parseInt(timeOfYear);
    interestRate = parseInt(interestRate) / 100 / timeOfYear;
    var tableData = [];
    var period = year * timeOfYear;
    var beginning_period = loan;
    var interest = 0;
    var principal = 0;
    var overdraft = loan;
    var per_instalment =
      (loan * interestRate) / (1 - 1 / (1 + interestRate) ** period);

    for (let index = 0; index < period; index++) {
      if (index != 0) {
        beginning_period = overdraft;
        interest = beginning_period * interestRate;
        principal = per_instalment - interest;
        per_instalment = per_instalment;
        overdraft -= principal;
        tableData.push([
          Math.ceil(beginning_period),
          Math.ceil(per_instalment),
          Math.ceil(interest),
          Math.ceil(principal),
          Math.ceil(overdraft),
        ]);
      } else {
        tableData.push(["", "", "", "", overdraft]);
      }
    }

    interest = per_instalment - overdraft;
    per_instalment = per_instalment;
    tableData.push([
      Math.ceil(overdraft),
      Math.ceil(per_instalment),
      Math.ceil(interest),
      Math.ceil(overdraft),
      Math.ceil(0),
    ]);

    this.setState({
      table: tableData,
    });
  };

  render() {
    const { loan, year, timeOfYear, interestRate } = this.props.calculatorParam;
    const { table } = this.state;

    return (
      <div
        style={{
          width: "100%",
          justifyContent: "center",
          alignItems: "center",
          padding: "24px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        <div style={{ display: "flex", flexDirection: "row" }}>
          <TextField
            label='貸款金額(萬元)：'
            style={{ marginRight: "20px" }}
            name='loan'
            value={loan}
            onChange={this.handleChangeText}
          />
          <TextField
            label='貸款貸幾年：'
            style={{ marginRight: "20px" }}
            name='year'
            value={year}
            onChange={this.handleChangeText}
          />
          <TextField
            label='年還款次數：'
            style={{ marginRight: "20px" }}
            name='timeOfYear'
            value={timeOfYear}
            onChange={this.handleChangeText}
          />
          <TextField
            label='年利率（％）：'
            style={{ marginRight: "20px" }}
            name='nterestRate'
            value={interestRate}
            onChange={this.handleChangeText}
          />
        </div>
        <CustomerTable rows={table} />
      </div>
    );
  }
}

export default connect((store) => ({ calculatorParam: store.calculatorParam }))(
  LoanCalculator
);
