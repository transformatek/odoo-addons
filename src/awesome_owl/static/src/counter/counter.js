/** @odoo-module */

import { Component, useState } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";

export class Counter extends Component {
  static template = "awesome_owl.Counter";
  static props = {
    onChange: { type: Function, optional: true },
  };

  setup() {
    this.state = useState({ value: 1 });
    this.orm = useService("orm");
  }

  async increment() {
    this.state.value = this.state.value + 1;
    // _______________________   Search _____________________________________

    const var1 = await this.orm.search("ir.model", [], { limit: 1 });
    console.log("### search________", var1);

    // _______________________   SearchRead _____________________________________

    const var2 = await this.orm.searchRead("product.template", [], []);
    console.log("### searchRead________", var2);

    // _______________________   Read _____________________________________

    const var3 = await this.orm.read("product.template", [1]);
    console.log("### read________", var3);

    // _______________________   Create _____________________________________

    const var4 = await this.orm.create("product.template", [
      {
        name: "New Product",
      },
    ]);
    console.log("### create________", var4);

    // _______________________   Write _____________________________________

    const var5 = await this.orm.write("product.template", [1], {
      name: "Product Updated",
    });
    console.log("### write________", var5);

    // _______________________   Delete _____________________________________

    try {
      const var6 = await this.orm.unlink("product.template", [4]);
      console.log("### delete________", var6);
    } catch (error) {
      console.error("Error deleted, no record");
    }

    if (this.props.onChange) {
      this.props.onChange();
    }
  }
}
