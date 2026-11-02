import { expect, test } from "vitest";
import { label } from "./status";

// 화면에 지정한 버전을 표시해야 한다.
test("renders the version", () => {
  expect(label("0.1.0")).toBe("kpais E2E 0.1.0");
});
