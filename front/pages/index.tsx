import _ from "lodash";
import styled from "styled-components"

import { Problem } from "../components"

const List = styled.ol`
  display: flex;
  flex-flow: row wrap;
  margin: 0;
  padding: 0;

  li {
    list-style: none;
  }
`;

function Home() {
  return <>
    <h1>Euler Project</h1>
    <List>
      {_.range(1, 50).map(n =>
        <Problem number={n} key={n} />
      )}
    </List>
  </>
}

export default Home
