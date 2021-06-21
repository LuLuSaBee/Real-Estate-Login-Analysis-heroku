import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import { useHistory } from "react-router-dom";
import { updateCalculatorParam } from "../redux/actions";

const googleMapUrl = (x, y) =>
  `https://www.google.com.tw/maps/search/${x},${y}/@${x},${y},17z`;

function EstateCard(props) {
  const classes = useStyles();
  const {
    location,
    coord_x,
    coord_y,
    zoning,
    build_area,
    tsign,
    bstate,
    tot_prc,
    unit_prc,
  } = props;
  const history = useHistory();

  return (
    <div className={classes.card}>
      <div className={classes.box}>
        <span>{build_area}坪</span>
      </div>
      <div className={classes.contianer}>
        <div className={classes.location}>{location}</div>
        <div>使用分區：{zoning}</div>
        <div>交易內容：{tsign}</div>
        <div>建物型態：{bstate}</div>
        <div
          onClick={() => {
            props.dispatch(updateCalculatorParam({ loan: tot_prc }));
            history.push("/calculator");
          }}
          className={classes.calculator}
        >
          成交價格：{tot_prc}萬元({unit_prc}萬/坪)
        </div>
        <div
          className={classes.link}
          onClick={() =>
            window.open(googleMapUrl(coord_x, coord_y), "_blank").focus()
          }
        >
          在Google地圖中打開
        </div>
      </div>
    </div>
  );
}

const useStyles = makeStyles(() => ({
  card: {
    width: "80%",
    height: "180px",
    backgroundColor: "white",
    borderRadius: "10px",
    boxShadow: "4px 4px 2px 1px rgb(0 0 0 / 0.1)",
    display: "flex",
    flexDirection: "row",
    marginBottom: "20px",
    padding: "10px",
    flex: 1,
  },
  box: {
    flex: 0.2,
    position: "relative",
    width: "100%",
    height: "100%",
    backgroundColor: "#99ccff",
    borderRadius: "10px",
    marginRight: "10px",
    color: "black",
    fontSize: "20pt",
    textAlign: "center",
    display: "flex",
    justifyContent: "center",
    alignItems: "center",
    fontWeight: 600,
  },
  contianer: {
    height: "100%",
    flex: 0.8,
    display: "flex",
    flexDirection: "column",
    position: "relative",
  },
  calculator: {
    cursor: "pointer",
  },
  location: {
    fontSize: "20pt",
    fontWeight: "bold",
  },
  link: {
    cursor: "pointer",
    alignSelf: "flex-end",
    justifySelf: "flex-end",
    position: "absolute",
    bottom: 0,
    right: 0,
  },
}));

export default connect()(EstateCard);
