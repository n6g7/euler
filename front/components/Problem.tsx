import { useEffect, useState } from "react";
import styled, { css } from "styled-components";

const statusColours = {
  loading: "#cccccc",
  success: "#78e08f",
  failure: "#e55039"
};

type Status = "loading" | "success" | "failure";

const Item = styled.li`
  align-items: center;
  background: ${p => statusColours[p.status]};
  border-radius: 2px;
  box-shadow: 0 1px 2px rgba(0,0,0,0.6);
  display: flex;
  justify-content: center;
  height: 24px;
  margin: 4px;
  position: relative;
  width: 24px;
`;

const Tooltip = styled.div`
  background: rgba(0, 0, 0, 0.7);
  border-radius: 3px;
  bottom: calc(100% + 4px);
  color: white;
  font-size: 0.9em;
  left: 0;
  min-width: 100px;
  padding: 4px;
  position: absolute;
  visibility: ${p => (p.show ? "visible" : "hidden")};

  &::after {
    border-color: rgba(0, 0, 0, 0.7) transparent;
    border-style: solid;
    border-width: 4px 4px 0;
    content: "";
    left: 8px;
    position: absolute;
    top: 100%;
  }
`;

function Problem({ number }) {
  const [status, setStatus] = useState<Status>("loading");
  const [solution, setSolution] = useState<number>(null);
  const [error, setError] = useState<string>(null);
  const [showTooltip, setTooltip] = useState(false);

  const loadSolution = async () => {
    let res
    try {
      res = await fetch(
        `https://4et3m03wb1.execute-api.eu-west-2.amazonaws.com/prod/problems/${number}`
      )
    }
    catch(error) {
      setStatus("failure")
      setError("server error")
      return
    }

    const data = await res.json()

    if (res.status === 200) {
      setStatus("success")
      setSolution(data.solution)
    }
    else {
      setStatus("failure")
      setError(data.error)
    }
  }

  useEffect(() => {
    loadSolution()
  }, [number]);

  return (
    <Item
      status={status}
      onMouseEnter={() => setTooltip(true)}
      onMouseLeave={() => setTooltip(false)}
    >
      {number}
      <Tooltip show={showTooltip}>
        <strong>Problem {number}</strong><br/>
        {status === "loading" && <em>loading...</em>}
        {status === "success" && `Solution: ${solution}`}
        {status === "failure" && `Error: ${error}`}
      </Tooltip>
    </Item>
  );
}

export default Problem;
