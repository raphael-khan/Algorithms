const nemo = ["nemo"]

function find_nemo(array) {
  let t0 = performance.now()
  for (let i = 0; i < array.length; i++) {
    if (array[i] === "nemo") {
      console.log("Found Nemo !")
    }
  }
  let t1 = performance.now()
  console.log("call to find nemo took" + (t1 - t0) + "milliseconds")
}

find_nemo(nemo)
