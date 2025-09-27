import CountUp from "react-countup";

export default function Counter({
  start = 0,
  end,
  duration = 2,
  suffix = "",
  prefix = "",
}) {
  return (
    <CountUp
      start={start}
      end={end}
      duration={duration}
      separator=","
      prefix={prefix}
      suffix={suffix}
    >
      {({ countUpRef }) => (
        <span ref={countUpRef} className="text-3xl font-bold text-blue-600" />
      )}
    </CountUp>
  );
}
