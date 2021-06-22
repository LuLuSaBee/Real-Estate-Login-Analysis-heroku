import React from "react";
import { Bar } from "react-chartjs-2";
import { connect } from "react-redux";

const rand = () => Math.floor(Math.random() * 255);

class HomePage extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;
  }

  barData = (data) => ({
    labels: data.map((d) => d.date),
    datasets: [
      {
        type: "line",
        label: "平均價格（萬元）",
        borderColor: `rgb(${rand()}, ${rand()}, ${rand()})`,
        borderWidth: 2,
        fill: false,
        data: data.map((d) => d.price / d.total),
      },
      {
        type: "bar",
        label: "成交數量",
        backgroundColor: `rgb(${rand()}, ${rand()}, ${rand()})`,
        data: data.map((d) => d.total),
        borderColor: "white",
        borderWidth: 2,
      },
    ],
  });

  render() {
    const { dashboardData } = this.props;
    const data = this.barData(dashboardData);

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
        <h1>全台2020不動產實價登錄分析</h1>
        <Bar data={data} />
      </div>
    );
  }
}

export default connect((store) => ({ dashboardData: store.dashboardData }))(
  HomePage
);
