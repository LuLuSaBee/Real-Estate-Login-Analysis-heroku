import React from "react";
import { connect } from "react-redux";
import EstateCard from "../components/EstateCard";
import InfiniteScroll from "react-infinite-scroller";
import { updateRealEstateData } from "../redux/actions";
import { getRealEstate } from "../helper/getDjangoData";

const numberOfaTime = 25;
class DataRetrieval extends React.Component {
  constructor(props) {
    super(props);
    this.props = props;
    this.state = {
      loading: false,
      hasMore: true,
    };
  }

  handleInfiniteOnLoad = () => {
    const { dispatch, realEstateData } = this.props;
    this.setState({
      loading: true,
    });
    getRealEstate(realEstateData.length - 1, (result) => {
      dispatch(updateRealEstateData(result));
      if (result.length < numberOfaTime) {
        this.setState({ hasMore: false, loading: false });
      } else {
        this.setState({ loading: false });
      }
    });
  };

  render() {
    const { realEstateData } = this.props;

    return (
      <InfiniteScroll
        initialLoad={false}
        pageStart={0}
        loadMore={this.handleInfiniteOnLoad}
        hasMore={!this.state.loading && this.state.hasMore}
        style={{
          backgroundColor: "#e6e6e6",
          width: "100%",
          justifyContent: "center",
          alignItems: "center",
          padding: "24px",
          display: "flex",
          flexDirection: "column",
        }}
      >
        {realEstateData.map((data) => (
          <EstateCard {...data} key={data.caseID} />
        ))}
      </InfiniteScroll>
    );
  }
}

export default connect((store) => ({
  realEstateData: store.realEstateData,
}))(DataRetrieval);
