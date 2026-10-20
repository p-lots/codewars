async function execute(action, nTimes){
  const actions = [];
  for (let i = 0; i < nTimes; i++) {
    actions.push(action());
  }
  return Promise.allSettled(actions);
}