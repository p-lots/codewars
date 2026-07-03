const createTemplate = template => {
  let templateCopy = template.slice();
  const templateMaker = templateObject => {
    for (const [key, value] of Object.entries(templateObject)) {
      templateCopy = templateCopy.replace(`{{${key}}}`, `${value}`);
    }
    templateCopy = templateCopy.replace(/{{\w+}}/g, "");
    return templateCopy;
  };
  return templateMaker;
};
